

import os
import sys
import subprocess
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

console = Console()

def get_scripts_dir():
    """Get the Python scripts directory."""
    if os.name == 'nt':
        return Path(sys.prefix) / 'Scripts'
    else:
        return Path(sys.prefix) / 'bin'

def add_to_path_windows(path: Path):
    """
    Adds a directory to the user's PATH on Windows using setx.
    We need to be careful not to exceed the 1024 character limit of setx.
    """
    try:
        # Get current user PATH
        current_path = subprocess.check_output('reg query "HKEY_CURRENT_USER\Environment" /v Path', shell=True)
        current_path = current_path.decode('utf-8').split()[-1]

        if str(path) not in current_path:
            # Append the new path
            new_path = f"{current_path};{str(path)}"
            if len(new_path) > 1024:
                print(f"Warning: New PATH exceeds 1024 characters. Manual addition required.")
                return

            subprocess.run(f'setx PATH "{new_path}"', shell=True, check=True)
            print(f"Successfully added {path} to your PATH.")
            print("Please restart your terminal for the changes to take effect.")
        else:
            print(f"{path} is already in your PATH.")

    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error adding to PATH: {e}")
        print(f"Please add '{path}' to your PATH manually.")

def add_to_path_posix(path: Path):
    """
    Adds a directory to the user's PATH on Linux/macOS by updating shell profiles.
    """
    home = Path.home()
    path_str = f'export PATH="$PATH:{str(path)}"'
    profiles = [home / '.bashrc', home / '.zshrc', home / '.profile']

    for profile in profiles:
        if profile.exists():
            with open(profile, 'r+') as f:
                if path_str not in f.read():
                    f.write(f'\n{path_str}\n')
                    print(f"Added to {profile}. Please restart your shell or run 'source {profile}'.")

def show_installation_success():
    console.print(Panel.fit(
        "[bold green]CliOps Successfully Installed![/bold green]\n\n"
        "[cyan]Quick Start:[/cyan]\n"
        "- [bold]cliops init[/bold] - Initialize configuration\n"
        "- [bold]cliops \"your prompt\"[/bold] - Optimize any prompt\n"
        "- [bold]cliops patterns[/bold] - View available patterns\n\n"
        "[dim]Run 'cliops --help' for full documentation[/dim]",
        border_style="green"
    ))

def main():
    scripts_dir = get_scripts_dir()
    if not scripts_dir.exists():
        print(f"Could not find scripts directory: {scripts_dir}")
        return

    print(f"Detected scripts directory: {scripts_dir}")

    if os.name == 'nt':
        add_to_path_windows(scripts_dir)
    elif os.name == 'posix':
        add_to_path_posix(scripts_dir)
    else:
        print(f"Unsupported OS: {os.name}")
        print(f"Please add '{scripts_dir}' to your PATH manually.")
    
    show_installation_success()

if __name__ == "__main__":
    main()
