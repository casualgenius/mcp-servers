# casual-mcp-server-time

Date and time utilities served via FastMCP.

## Tools

- **current_time** - Get the current time in a given timezone.
- **time_since** - Human readable time elapsed since a given date.
- **add_days** - Add days to today and return the future date.
- **subtract_days** - Subtract days from today and return the past date.
- **date_diff** - Number of days between two dates.
- **next_weekday** - Date of the next occurrence of a weekday.
- **is_leap_year** - Check if a year is a leap year.
- **week_number** - ISO week number for a date.
- **parse_human_date** - Parse a natural language date description.

## Run with Python

```bash
cd servers/time
uv pip install --system .
python -m casual_mcp_server_time.server
```

## Run with `uvx`

```bash
uvx casual-mcp-server-time
```

## Run with Docker

```bash
docker build -t casual-mcp-server-time .
docker run -p 8000:8000 casual-mcp-server-time
```
