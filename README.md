# AI21 Maestro Workshop



## Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) - A fast Python package installer and resolver

### Installing uv

If you don't have `uv` installed, you can install it with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or on macOS with Homebrew:

```bash
brew install uv
```

## Getting Started

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd Maestro-Testing
   ```

2. **Initialize the project**:
   ```bash
   ./init.sh
   ```
   
   This script will:
   - Check if `uv` is installed
   - Create a virtual environment in `.venv` (if it doesn't exist)
   - Install all dependencies from `pyproject.toml`

3. **Activate the virtual environment**:
   ```bash
   source .venv/bin/activate
   ```

4. **Start coding!** 🚀

## Project Structure

```
Maestro-Testing/
├── .venv/              # Virtual environment (created by init.sh)
├── .python-version     # Python version specification (3.12)
├── pyproject.toml      # Project dependencies and configuration
├── init.sh             # Project initialization script
└── README.md           # This file
```

## Common Commands

### Sync dependencies
```bash
uv sync
```

### Add a new dependency
```bash
uv add <package-name>
```

### Remove a dependency
```bash
uv remove <package-name>
```

### Run Python
```bash
# Make sure virtual environment is activated
source .venv/bin/activate
python your_script.py
```

## 📚 Additional Resources

* [AI21 Studio Docs](https://docs.ai21.com) – API reference, guides, and tutorials.
* [AI21 Blog](https://www.ai21.com/blog) – product updates and deep dives.
* [AI21 SDK Repo](https://github.com/AI21Labs/ai21-python) – the latest info on the Python SDK.