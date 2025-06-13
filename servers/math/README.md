# casual-mcp-server-math

Math and conversion utilities served via FastMCP.

## Tools

- **add** - Add two numbers.
- **subtract** - Subtract one number from another.
- **multiply** - Multiply two numbers.
- **divide** - Divide a by b.
- **percentage_diff** - Calculate the percentage difference between two values.
- **round_number** - Round a number to a given number of decimal places.

## Run with Python

```bash
cd servers/math
uv pip install --system .
python -m casual_mcp_server_math.server
```

## Run with `uvx`

```bash
uvx casual-mcp-server-math
```

## Run with Docker

```bash
docker build -t casual-mcp-server-math .
docker run -p 8000:8000 casual-mcp-server-math
```
