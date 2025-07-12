import argparse
import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text
from rich.layout import Layout

from core.config import Config
from core.state import CLIState
from core.patterns import PatternRegistry
from core.analyzer import PromptAnalyzer
from core.optimizer import PromptOptimizer
from presets import suggest_preset_from_prompt, apply_preset_interactive

console = Console()

def _define_subparsers(subparsers):
    # Optimize command
    optimize_parser = subparsers.add_parser("optimize", aliases=['opt'], help="Optimize a raw prompt using a specified pattern.")
    optimize_parser.add_argument("prompt", type=str, nargs='?', help="The raw prompt string to optimize. If omitted, tries to read from stdin.")
    optimize_parser.add_argument("--pattern", type=str, required=False, help="The name of the optimization pattern to apply.")
    optimize_parser.add_argument("--dry-run", action="store_true", help="Show parsed fields and final template before generation.")
    
    # Common override arguments
    optimize_parser.add_argument("--directive", type=str, help="Override the 'DIRECTIVE' field.")
    optimize_parser.add_argument("--scope", type=str, help="Override the 'SCOPE' field.")
    optimize_parser.add_argument("--constraints", type=str, help="Override the 'CONSTRAINTS' field.")
    optimize_parser.add_argument("--output-format", type=str, help="Override the 'OUTPUT FORMAT' field.")
    optimize_parser.add_argument("--success-criteria", type=str, help="Override the 'SUCCESS CRITERIA' field.")
    optimize_parser.add_argument("--code", type=str, help="Override the 'CODE' block content.")
    optimize_parser.add_argument("--context", type=str, help="Override the 'CONTEXT' for context-aware patterns.")
    optimize_parser.add_argument("--current-focus", type=str, help="Override 'CURRENT FOCUS' for context-aware patterns.")
    optimize_parser.add_argument("--mindset", type=str, help="Override 'MINDSET' for context-aware patterns.")

    # Analyze command
    analyze_parser = subparsers.add_parser("analyze", aliases=['an'], help="Analyze a raw prompt for optimization recommendations.")
    analyze_parser.add_argument("prompt", type=str, nargs='?', help="The raw prompt string to analyze.")

    # Patterns command
    patterns_parser = subparsers.add_parser("patterns", aliases=['ls'], help="List available optimization patterns.")
    patterns_parser.add_argument("pattern_name", nargs="?", type=str, help="Optional: Name of a specific pattern to get details for.")

    # State command
    state_parser = subparsers.add_parser("state", help="Manage persistent CLI state.")
    state_subparsers = state_parser.add_subparsers(dest="state_command", help="State commands")

    state_set_parser = state_subparsers.add_parser("set", help="Set a key-value pair in the CLI state.")
    state_set_parser.add_argument("key", type=str, help="The key for the state variable.")
    state_set_parser.add_argument("value", type=str, help="The value to set.")

    state_show_parser = state_subparsers.add_parser("show", help="Show the current CLI state.")
    state_clear_parser = state_subparsers.add_parser("clear", help="Clear all entries from the CLI state.")

    # Init command
    init_parser = subparsers.add_parser("init", help="Initialize CliOps configuration files.")

def _run_init_command(cli_state: CLIState, pattern_registry: PatternRegistry):
    """Handles the 'cliops init' command to set up config files."""
    from core.welcome import show_welcome_banner, show_first_run_tips
    
    show_welcome_banner()
    console.print(Panel("[bold green]Initializing CliOps Configuration[/bold green]", expand=False, border_style="green"))
    
    state_file = Config.get_state_file_path()
    is_first_run = not state_file.exists() or cli_state.state == {}
    
    if is_first_run:
        state_file.parent.mkdir(parents=True, exist_ok=True)
        cli_state.clear()
        console.print(f"Created CLI state file: [bold cyan]{state_file}[/bold cyan]", style="green")
        console.print(Panel("[bold green]Initialization complete![/bold green]", expand=False, border_style="green"))
        show_first_run_tips()
    else:
        console.print(f"CLI state file already exists at [bold cyan]{state_file}[/bold cyan].", style="dim")
        console.print(Panel("[bold green]Initialization complete![/bold green]", expand=False, border_style="green"))

def main():
    # Create a dummy parser to peek at the arguments
    temp_parser = argparse.ArgumentParser(add_help=False)
    temp_parser.add_argument("first_arg", nargs='?', help=argparse.SUPPRESS)
    temp_parser.add_argument("--verbose", action="store_true", help=argparse.SUPPRESS)
    
    temp_args, remaining_argv = temp_parser.parse_known_args(sys.argv[1:])
    verbose_mode = temp_args.verbose

    known_commands = ["optimize", "opt", "analyze", "an", "patterns", "ls", "state", "init"]

    # Check if the first argument looks like a prompt
    is_direct_prompt = (temp_args.first_arg and
                        temp_args.first_arg not in known_commands and
                        not temp_args.first_arg.startswith('-'))

    if is_direct_prompt:
        new_argv = ["optimize", temp_args.first_arg] + remaining_argv
        sys.argv = [sys.argv[0]] + new_argv
    
    # Set up the real parser
    parser = argparse.ArgumentParser(
        description="CliOps: Command Line Interface for Prompt Optimization and State Management (v3.2)",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output for debugging.")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    _define_subparsers(subparsers)
    
    args = parser.parse_args()

    if hasattr(args, 'verbose') and args.verbose:
        verbose_mode = True

    cli_state = CLIState(Config.get_state_file_path())
    pattern_registry = PatternRegistry(cli_state)

    # Handle cases where prompt might be piped via stdin
    if hasattr(args, 'prompt') and args.prompt is None and not sys.stdin.isatty():
        args.prompt = sys.stdin.read().strip()
        if not args.prompt:
            console.print("[bold red]Error:[/bold red] No prompt provided via argument or stdin.", style="red")
            sys.exit(1)
    elif hasattr(args, 'prompt') and args.prompt is None and sys.stdin.isatty() and args.command in ["optimize", "analyze"]:
        console.print(f"[bold red]Error:[/bold red] Missing prompt argument for '{args.command}' command.", style="red")
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Intelligent pattern selection
    if args.command in ["optimize", "opt"] and (not hasattr(args, 'pattern') or args.pattern is None):
        default_pattern = cli_state.get("DEFAULT_PATTERN")
        if default_pattern and pattern_registry.get_pattern(default_pattern):
            args.pattern = default_pattern
        else:
            # Auto-select best pattern based on prompt complexity
            if hasattr(args, 'prompt') and args.prompt and len(args.prompt) > 100:
                args.pattern = "adaptive_generation"
            elif hasattr(args, 'prompt') and args.prompt and any(word in args.prompt.lower() for word in ['api', 'endpoint', 'function', 'class', 'implement']):
                args.pattern = "precision_engineering"
            else:
                args.pattern = "adaptive_generation"

    if args.command in ["optimize", "opt"]:
        overrides = {k: v for k, v in vars(args).items() if v is not None and k not in ['command', 'prompt', 'pattern', 'dry_run', 'verbose']}
        
        try:
            optimizer = PromptOptimizer(pattern_registry, cli_state, verbose=verbose_mode)
            optimized_prompt = optimizer.optimize_prompt(args.prompt, args.pattern, overrides, args.dry_run)
            
            if not args.dry_run:
                # Extract metadata for display
                from core.intelligence import PromptIntelligence
                domain = PromptIntelligence.detect_domain(args.prompt)
                complexity = PromptIntelligence.assess_complexity(args.prompt)
                
                # Enhanced header with metadata
                console.print(Panel.fit(
                    f"[bold green]Optimized Prompt[/bold green]\n"
                    f"[dim]Domain: {domain} | Pattern: {args.pattern} | Complexity: {complexity}[/dim]",
                    border_style="green"
                ))
                
                # Display the optimized prompt
                console.print(optimized_prompt)
                
                # Enhanced footer
                console.print(Panel.fit("[dim]Prompt Optimization Complete[/dim]", border_style="dim"))
            
        except ValueError as e:
            from core.errors import show_error
            if "Pattern" in str(e) and "not found" in str(e):
                pattern_name = str(e).split("'")[1] if "'" in str(e) else "unknown"
                show_error("pattern_not_found", pattern=pattern_name)
            else:
                console.print(f"[bold red]Error:[/bold red] {e}", style="red")
            sys.exit(1)
        
    elif args.command in ["analyze", "an"]:
        analyzer = PromptAnalyzer(pattern_registry)
        analyzer.analyze_prompt(args.prompt)
    elif args.command in ["patterns", "ls"]:
        if args.pattern_name:
            pattern_registry.show_pattern_details(args.pattern_name)
        else:
            pattern_registry.list_patterns()
    elif args.command == "state":
        if args.state_command == "set":
            cli_state.set(args.key, args.value)
        elif args.state_command == "show":
            cli_state.show()
        elif args.state_command == "clear":
            cli_state.clear()
    elif args.command == "init":
        _run_init_command(cli_state, pattern_registry)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()