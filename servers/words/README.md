# casual-mcp-server-words

Dictionary and thesaurus utilities using the Free Dictionary API served via FastMCP.

## Tools

- **define** - Retrieve definitions of an English word.
- **example_usage** - Example usage sentences for a word.
- **synonyms** - Synonyms for a word.

## Run with Python

```bash
cd servers/words
uv pip install --system .
python -m casual_mcp_server_words.server
```

## Run with `uvx`

```bash
uvx casual-mcp-server-words
```

## Run with Docker

```bash
docker build -t casual-mcp-server-words .
docker run -p 8000:8000 casual-mcp-server-words
```
