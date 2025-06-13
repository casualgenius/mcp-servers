FROM python:3.11-slim AS base

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the Code
WORKDIR /app
COPY . /app

# Set shared default environment variables
ENV MCP_TRANSPORT=stdio
ENV MCP_PORT=8000
ENV MCP_HOST=0.0.0.0

# Change to Server Folder
WORKDIR /app/servers/words

# Install Deps
RUN uv sync --locked

# Run the Server
CMD uv run casual-mcp-server-words --transport ${MCP_TRANSPORT:-stdio} --port ${MCP_PORT:-8000} --host ${MCP_HOST:-0.0.0.0}
