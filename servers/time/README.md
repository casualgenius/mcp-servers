# Time and Date MCP Server

Date and time utilities served via FastMCP.

The server can be accessed locally over Stdio or remotely over SSE/Streamable HTTP.

## Tools

The tools exposed by the MCP server include:

- **current_time** - Get the current time in a given timezone.
- **time_since** - Human readable time elapsed since a given date.
- **add_days** - Add days to today and return the future date.
- **subtract_days** - Subtract days from today and return the past date.
- **date_diff** - Number of days between two dates.
- **next_weekday** - Date of the next occurrence of a weekday.
- **is_leap_year** - Check if a year is a leap year.
- **week_number** - ISO week number for a date.
- **parse_human_date** - Parse a natural language date description.

## Configuration

### Local Time Zone

The local time zone can be set using the environmental variable `LOCAL_TIME_ZONE`.

It takes a [IANA Timezone](https://nodatime.org/TimeZones), if not given it will default to `Etc/UTC`.

## Running the Server

### Run from source

```bash
cd servers/time
uv pip install --system .
casual-mcp-server-time
```

### Run with `uvx`

Run the package directly using `uvx`

```bash
uvx casual-mcp-server-time
```

## Run with Docker

You can run 

```bash
docker build -t casual-mcp-server-time .
docker run casual-mcp-server-time
```
