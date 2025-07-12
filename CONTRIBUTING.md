# Contributing to cliops

We welcome contributions to cliops! This guide will help you get started.

## Quick Links

- **Documentation**: [cliops.fun/docs](https://cliops.fun/docs)
- **Community**: [cliops.fun/join](https://cliops.fun/join)
- **GitHub**: [github.com/thatmabd](https://github.com/thatmabd)

## Ways to Contribute

- **Bug Reports**: Report issues and bugs
- **Feature Requests**: Suggest new features
- **Code Contributions**: Submit pull requests
- **Documentation**: Improve docs and guides
- **Plugins**: Create and share plugins
- **Community**: Help others in discussions

## Development Setup

### Prerequisites

- Python 3.8+
- Git
- pip

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/thatmabd/cliops
cd cliops

# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python run_tests.py
```

## Code Standards

### Python Style

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for public functions
- Keep functions focused and small

### Code Quality

```bash
# Run linting
flake8 cliops/

# Run type checking
mypy cliops/

# Run tests with coverage
pytest --cov=cliops
```

### Testing

- Write tests for new features
- Maintain test coverage above 90%
- Test edge cases and error conditions
- Use descriptive test names

```python
def test_optimizer_handles_empty_prompt():
    """Test that optimizer gracefully handles empty prompts."""
    # Test implementation
```

## Submitting Changes

### Pull Request Process

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Submit** pull request

### Branch Naming

- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring

### Commit Messages

Use clear, descriptive commit messages:

```
feat: add plugin system for custom patterns
fix: resolve memory leak in cache manager
docs: update installation guide
test: add comprehensive optimizer tests
```

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Tests pass locally
- [ ] New tests added
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
```

## Plugin Development

### Creating Plugins

```bash
# Generate plugin template
cliops plugin create my_contribution

# Edit plugin
# ~/.cliops/plugins/my_contribution.py

# Test plugin
cliops plugin enable my_contribution
cliops patterns  # Should show your patterns
```

### Plugin Guidelines

- Follow the `PluginInterface`
- Provide clear pattern descriptions
- Include usage examples
- Test with various inputs
- Document configuration options

### Sharing Plugins

1. Create separate repository for plugin
2. Include comprehensive README
3. Add examples and tests
4. Share in community: [cliops.fun/join](https://cliops.fun/join)

## Documentation

### Documentation Structure

```
docs/
├── README.md              # Documentation index
├── getting-started.md     # Installation and first steps
├── user-guide.md         # Complete user guide
├── plugin-development.md  # Plugin creation guide
├── configuration.md      # Configuration reference
├── api-reference.md      # API documentation
└── troubleshooting.md    # Common issues
```

### Writing Guidelines

- Use clear, concise language
- Include code examples
- Provide step-by-step instructions
- Link to related sections
- Test all examples

## Issue Reporting

### Bug Reports

Include:
- cliops version
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages/logs

### Feature Requests

Include:
- Use case description
- Proposed solution
- Alternative solutions considered
- Additional context

## Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Help others learn and grow
- Provide constructive feedback
- Focus on the issue, not the person

### Communication

- **GitHub Issues**: Bug reports and feature requests
- **Pull Requests**: Code contributions and reviews
- **Community**: [cliops.fun/join](https://cliops.fun/join)
- **Documentation**: [cliops.fun/docs](https://cliops.fun/docs)

## Release Process

### Versioning

cliops follows semantic versioning:
- `MAJOR.MINOR.PATCH`
- Major: Breaking changes
- Minor: New features (backward compatible)
- Patch: Bug fixes

### Release Checklist

- [ ] All tests pass
- [ ] Documentation updated
- [ ] Version bumped
- [ ] Changelog updated
- [ ] Release notes prepared

## Getting Help

### Development Questions

- Check existing issues and discussions
- Join community: [cliops.fun/join](https://cliops.fun/join)
- Review documentation: [cliops.fun/docs](https://cliops.fun/docs)

### Mentorship

New contributors welcome! We provide:
- Code review and feedback
- Architecture guidance
- Testing assistance
- Documentation help

## Recognition

Contributors are recognized through:
- GitHub contributor list
- Release notes mentions
- Community highlights
- Documentation credits

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to cliops! 🚀

**Links:**
- **Documentation**: [cliops.fun/docs](https://cliops.fun/docs)
- **Community**: [cliops.fun/join](https://cliops.fun/join)
- **GitHub**: [github.com/thatmabd](https://github.com/thatmabd)