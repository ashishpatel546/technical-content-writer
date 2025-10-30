#!/bin/bash

# Technical Content Writer - Gradio App Launcher
# This script sets up the virtual environment and runs the Gradio application

set -e  # Exit on any error

echo "🚀 Starting Technical Content Writer setup..."

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "📁 Working directory: $SCRIPT_DIR"

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ Error: uv is not installed. Please install uv first."
    echo "   Visit: https://github.com/astral-sh/uv"
    exit 1
fi

echo "✅ uv is available"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "🔧 Creating virtual environment..."
    uv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Install dependencies
echo "📦 Installing dependencies..."
uv sync
echo "✅ Dependencies installed successfully"

# Activate virtual environment and run the app
echo "🎯 Activating virtual environment and starting Gradio app..."
echo "📱 The app will be available at http://localhost:7860"
echo "🛑 Press Ctrl+C to stop the application"
echo ""

# Activate the virtual environment and run the app
source .venv/bin/activate && python gradio_app.py