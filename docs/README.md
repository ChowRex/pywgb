# Documentation

This directory contains the Sphinx documentation for pywgb.

## Building the Documentation

### Prerequisites

Install documentation dependencies:

```bash
pip install -e ".[docs]"
```

### Build HTML Documentation

```bash
cd docs
make html
```

The generated HTML documentation will be in `docs/_build/html/`.

Open `docs/_build/html/index.html` in your browser to view.

### Other Formats

```bash
# PDF (requires LaTeX)
make latexpdf

# Plain text
make text

# Man pages
make man

# Clean build artifacts
make clean
```

## Documentation Structure

```
docs/
├── conf.py              # Sphinx configuration
├── index.rst            # Main documentation page
├── api/                 # API reference documentation
│   ├── modules.rst      # Module overview
│   ├── smartbot.rst     # SmartBot documentation
│   ├── bots.rst         # Bot classes documentation
│   └── decorators.rst   # Decorators documentation
├── Makefile             # Build automation (Unix)
└── make.bat             # Build automation (Windows)
```

## Documentation Style

This project uses **Sphinx** with **Google-style docstrings** (via Napoleon extension).

### Docstring Format

```python
def function(arg1: str, arg2: int) -> bool:
    """
    Short description.
    
    Longer description with more details about the function's
    behavior and usage.
    
    Args:
        arg1 (str): Description of arg1.
        arg2 (int): Description of arg2.
    
    Returns:
        bool: Description of return value.
    
    Raises:
        ValueError: When validation fails.
        IOError: When operation fails.
    
    Example:
        ::
        
            result = function("test", 42)
            print(result)
    
    Note:
        Additional notes or warnings.
    
    See Also:
        :func:`related_function`: Related functionality
    """
```

## Contributing to Documentation

1. Update docstrings in source code following the Google style
2. Add new `.rst` files for new sections if needed
3. Rebuild documentation to verify changes
4. Check for warnings during build
5. Review generated HTML for formatting issues

## Viewing Documentation Online

Once published, documentation will be available at:
- Read the Docs: (to be configured)
- GitHub Pages: (to be configured)
