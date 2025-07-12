# cliops - Command Line Interface for Prompt Optimization

1- Install cliops in your terminal.

2- Open your project inside any IDE or Navigate to your project cd your-awesome-project.

3- Start optimizing with cliops by just saying; cliops and your prompt between two ""
cliops "your main prompt"

A powerful CLI tool for structured, pattern-based prompt optimization and state management.

[![GitHub](https://img.shields.io/badge/GitHub-thatmabd-blue)](https://github.com/thatmabd)
[![Documentation](https://img.shields.io/badge/Docs-cliops.fun-green)](https://cliops.fun/docs)
[![Community](https://img.shields.io/badge/Join-cliops.fun-orange)](https://cliops.fun/join)

## Features

- **Pattern-based optimization**: Apply proven prompt engineering patterns
- **State management**: Persistent CLI state for project context
- **Rich terminal UI**: Beautiful output with syntax highlighting
- **Extensible**: Add custom patterns and plugins
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Performance optimized**: Advanced caching and memory management
- **Plugin system**: Extend functionality with custom plugins

## Quick Start

```bash
# Install
pip install cliops

# Initialize
cliops init

# Optimize a prompt
cliops "Create a user authentication endpoint"

# Analyze a prompt
cliops analyze "Make this code better"

# List patterns
cliops patterns
```

## Installation

```bash
pip install .
```

The installer will attempt to add the necessary directory to your system's PATH. Please restart your terminal after installation.

## Usage

### Basic Commands

```bash
# Direct prompt optimization
cliops "Fix this bug in my React component"

# With specific pattern
cliops optimize "Refactor this function" --pattern precision_engineering

# Analyze prompt for improvements
cliops analyze "Create API endpoint"

# List available patterns
cliops patterns

# Manage state
cliops state set ARCHITECTURE "React + Node.js"
cliops state show

# Plugin management
cliops plugin list
cliops plugin create my_plugin
```

### Advanced Features

```bash
# Context-aware optimization
cliops "Create dashboard" --context "React + TypeScript"

# Dry run to preview
cliops "Test prompt" --dry-run

# Override specific fields
cliops "API task" --constraints "RESTful design" --output-format "JSON"
```

## Configuration

cliops uses YAML-based configuration with environment support:

```yaml
# ~/.cliops/config.yaml
environment: production
logging:
  level: INFO
optimization:
  cache_enabled: true
  default_pattern: adaptive_generation
performance:
  memory_limit_mb: 512
```

## Plugin Development

Create custom plugins to extend cliops:

```bash
# Create plugin template
cliops plugin create my_plugin

# Edit the generated template
# ~/.cliops/plugins/my_plugin.py

# Enable plugin
cliops plugin enable my_plugin
```

## Documentation

- **Full Documentation**: [cliops.fun/docs](https://cliops.fun/docs)
- **API Reference**: Comprehensive module documentation
- **Plugin Development Guide**: Create custom extensions
- **Configuration Reference**: All settings explained

## Community

- **Join Community**: [cliops.fun/join](https://cliops.fun/join)
- **GitHub**: [github.com/thatmabd](https://github.com/thatmabd)
- **Issues & Support**: GitHub Issues
- **Contributions**: Pull requests welcome

## Testing

```bash
python run_tests.py
```

## License

MIT License

## Architecture

cliops is built with:
- **Intelligence System**: Domain detection and pattern suggestion
- **Context Optimizer**: Project-aware prompt enhancement
- **Performance Monitor**: Memory and execution optimization
- **Plugin Framework**: Extensible architecture
- **Configuration Manager**: Environment-based settings

For detailed architecture documentation, visit [cliops.fun/docs](https://cliops.fun/docs).
