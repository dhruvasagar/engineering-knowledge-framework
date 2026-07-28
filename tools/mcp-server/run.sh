#!/usr/bin/env bash
# Run the Engineering Knowledge Framework MCP Server
set -e

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
VENV="$REPO_ROOT/tools/mcp-server/.venv"

if [ ! -d "$VENV" ]; then
    echo "Creating virtual environment..."
    uv venv "$VENV"
    uv pip install --python "$VENV/bin/python" mcp
fi

exec "$VENV/bin/python" "$REPO_ROOT/tools/mcp-server/server.py" "$@"
