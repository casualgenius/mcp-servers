# Math MCP Server

[![PyPI](https://img.shields.io/pypi/v/casual-mcp-server-math.svg)](https://pypi.org/project/casual-mcp-server-math/)
[![License](https://img.shields.io/github/license/casualgenius/mcp-servers)](https://github.com/casualgenius/mcp-servers/blob/main/LICENSE)

> An MCP server providing math tools for LLMs.

---

## Overview

The Math MCP Server provides math utilities for language models and AI assistants. It allows tools like `add`, `subtract`, `percentage_diff` to be called programmatically via Stdio or Streamable HTTP.

---

## Tools

The tools exposed by the MCP server include:

- **add** - Add two numbers.
- **subtract** - Subtract one number from another.
- **multiply** - Multiply two numbers.
- **divide** - Divide a by b.
- **percentage_diff** - Calculate the percentage difference between two values.
- **round_number** - Round a number to a given number of decimal places.

---

## 🛠️ Installation

### Local Development (via `uv`)

From this directory:

```bash
uv sync --locked
uv tool install .
```

### Docker Build

From the root of the repository:

```bash
docker build -f servers/math/Dockerfile -t casual-mcp-server-math .
```

---

## ▶️ Running the Server

### ➤ Stdio Mode

#### From Source

Install for local development and then configure:

```json
{
  "mcpServers": {
    "math": {
      "command": "uv",
      "args": ["tool", "run", "casual-mcp-server-math"]
    }
  }
}
```

#### Using `uvx`

```json
{
  "mcpServers": {
    "math": {
      "command": "uvx",
      "args": ["casual-mcp-server-math"]
    }
  }
}
```

#### Docker

```json
{
  "mcpServers": {
    "math": {
      "command": "docker",
      "args": ["run", "--rm", "casual-mcp-server-math"]
    }
  }
}
```

---

### ➤ Streamable HTTP Mode

#### From Source

```bash
uv run casual-mcp-server-math --transport streamable-http
```

With port/host overrides:

```bash
uv run casual-mcp-server-math --transport streamable-http --port 9000 --host 0.0.0.0
```

#### Using `uvx`

```bash
uvx casual-mcp-server-math --transport streamable-http
```

You can use the same port/host overrides as above

#### Docker

```bash
docker run -e MCP_TRANSPORT=streamable-http -e MCP_PORT=9000 -p 9000:9000 casual-mcp-server-math
```

##### Configuration

```json
{
  "mcpServers": {
    "math": {
      "type": "streamable-http",
      "url": "http://localhost:9000"
    }
  }
}
```

---

## 📜 License

MIT – [LICENSE](https://github.com/casualgenius/mcp-servers/blob/main/LICENSE)

---

## 📦 PyPI

Published at: [https://pypi.org/project/casual-mcp-server-math/](https://pypi.org/project/casual-mcp-server-math/)
