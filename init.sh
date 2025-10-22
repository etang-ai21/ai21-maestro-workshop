#!/bin/bash

# Python project initialization script using uv

set -e

echo "🚀 Initializing Python project with uv..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Please install it first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment in .venv..."
    uv venv .venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Install dependencies using uv
echo "📥 Installing dependencies..."
uv sync

echo "✨ Project initialization complete!"
echo ""
echo "To activate the virtual environment, run:"
echo "  source .venv/bin/activate"

