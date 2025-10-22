# AI21 Maestro Workshop

Welcome to the AI21 Maestro Workshop! This hands-on workshop will guide you through building production-grade AI applications using AI21's Maestro platform.

## Workshop Modules

### [Module 0: Setup](modules/module_00_setup/)
Get your development environment configured and verify your API credentials.

### [Module 1: Maestro Validated Output (MVO)](modules/module_01_mvo/)
Learn how to enforce complex constraints and prevent hallucinations using Maestro's Generate → Validate → Fix cycle. Build a travel booking data extractor that reliably follows strict "no inference" rules.

**Key Topics:**
- Validated Output fundamentals
- Requirements definition and scoring
- Budget tier selection
- Hallucination prevention
- Production-grade data extraction

### [Module 2: RAG with File Search](modules/module_02_rag/)
Build conversational AI that answers questions grounded in your own documents using Maestro's RAG Engine. Create a technical troubleshooting assistant with semantic search and source citations.

**Key Topics:**
- Retrieval-Augmented Generation (RAG)
- File Library and document indexing
- Multi-turn conversations
- Grounded responses with source citations
- Semantic search capabilities

### [Module 3: MCP Servers](modules/module_03_mcp/)
Integrate AI with your existing systems using the Model Context Protocol. Build a remote MCP server for employee management that Maestro can query through natural language.

**Key Topics:**
- Model Context Protocol (MCP) architecture
- Remote MCP server development
- Tool discovery and dynamic invocation
- Multi-tool query handling
- Security and authentication best practices

### [Module 4: Use Case Implementation](modules/module_04_use_case/)
Apply everything you've learned to build a complete AI application combining MVO, RAG, and MCP.

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
ai21-maestro-workshop/
├── .venv/                          # Virtual environment (created by init.sh)
├── modules/                        # Workshop modules
│   ├── module_00_setup/           # Setup and configuration
│   │   ├── setup.ipynb
│   │   └── README.md
│   ├── module_01_mvo/             # Maestro Validated Output
│   │   ├── mvo.ipynb
│   │   └── README.md
│   ├── module_02_rag/             # RAG with File Search
│   │   ├── rag.ipynb
│   │   ├── README.md
│   │   └── SYSTEM AIR CONDITIONER.pdf
│   ├── module_03_mcp/             # MCP Servers
│   │   ├── mcp.ipynb
│   │   ├── mcp_server.py
│   │   └── README.md
│   └── module_04_use_case/        # Final use case implementation
├── pyproject.toml                  # Project dependencies and configuration
├── uv.lock                         # Dependency lock file
├── init.sh                         # Project initialization script
└── README.md                       # This file
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