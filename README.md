# CEN4090L Project G26 - Personal Assistant MCP

This repository contains the CEN4090L Group 26 project - a collection of Model Context Protocol (MCP) servers that provide various tools for a personal assistant system. Each MCP server offers specialized functionality that can be integrated with Claude Desktop and other MCP-compatible clients.

## Requirements

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) package manager

Dependencies are managed in individual `pyproject.toml` files within each MCP server directory.

---

## Available MCP Servers

### 1. **Weather-Info**
Provides weather information using the AccuWeather API.

**Tools:**
- `get_current_weather(city)` - Get current weather conditions for a city
- `get_weather_forecast(city)` - Get 5-day weather forecast for a city

**Setup:**
- Requires `API_KEY` environment variable (AccuWeather API key)
- Dependencies: `aiohttp`, `python-dotenv`, `fastmcp`

**Configuration:**
```json
"Weather-Info": {
  "command": "uv",
  "args": [
    "--directory",
    "/absolute/path/to/Personal-Assistant-MCP/Weather-Info",
    "run",
    "main.py"
  ]
}
```

---

### 2. **Gmail-MCP**
Gmail and Google Calendar integration for managing emails and calendar events.

**Tools:**
- **Gmail:**
  - `gmail_send(to, subject, body, html)` - Send emails
  - `gmail_search(query, limit)` - Search emails with Gmail query syntax
  - `gmail_delete_tool(message_id, permanent)` - Delete or trash messages
  - `gmail_list_unread_tool(limit, in_inbox)` - List unread messages
  - `gmail_reply_tool(thread_id, body, html, reply_all)` - Reply to email threads

- **Calendar:**
  - `calendar_list_tool(limit)` - List upcoming calendar events
  - `calendar_create_tool(summary, start_time, duration_minutes, description, location)` - Create calendar events
  - `calendar_delete_tool(event_id)` - Delete calendar events

**Setup:**
- Requires Google OAuth credentials (`credentials.json`)
- Token stored in `token.json` (auto-generated on first run)
- Dependencies: `google-api-python-client`, `google-auth-oauthlib`, `fastmcp`, `python-dotenv`

**Configuration:**
```json
"Gmail-Tools": {
  "command": "uv",
  "args": [
    "--directory",
    "/absolute/path/to/Personal-Assistant-MCP/Gmail-MCP",
    "run",
    "main.py"
  ]
}
```

---

### 3. **Stock-MCP**
Stock market information using Alpha Vantage API.

**Tools:**
- `global_quote(symbol)` - Get latest stock quote
- `time_series_daily(symbol, adjusted, outputsize)` - Get daily time series data
- `rsi(symbol, interval, time_period, series_type)` - Calculate RSI technical indicator

**Setup:**
- Requires `STOCK_API` environment variable (Alpha Vantage API key)
- Dependencies: `fastmcp`, `python-dotenv`, `requests`

**Configuration:**
```json
"Stock-MCP": {
  "command": "uv",
  "args": [
    "--directory",
    "/absolute/path/to/Personal-Assistant-MCP/Stock-MCP",
    "run",
    "stockinfo.py"
  ]
}
```

---

### 4. **News-MCP**
Latest news articles using NewsAPI.

**Tools:**
- `get_latest_news(query, hours, max_results, language)` - Get recent news articles about a topic
- `get_headlines(country, category, max_results)` - Get top headlines by country/category

**Setup:**
- Requires `NEWS_API_KEY` environment variable (NewsAPI key)
- Dependencies: `fastmcp`, `python-dotenv`, `aiohttp`

**Configuration:**
```json
"News-MCP": {
  "command": "uv",
  "args": [
    "--directory",
    "/absolute/path/to/Personal-Assistant-MCP/News-MCP",
    "run",
    "news_mcp/main.py"
  ]
}
```

---

### 5. **News-MCP-User**
Alternative news provider using Google News RSS (no API key required).

**Tools:**
- `get_latest_news_about(query, max_results, hl, gl, ceid)` - Get latest news from Google News RSS

**Setup:**
- No API key required
- Dependencies: `fastmcp`, `aiohttp`, `feedparser`

**Configuration:**
```json
"News-MCP-User": {
  "command": "uv",
  "args": [
    "--directory",
    "/absolute/path/to/Personal-Assistant-MCP/News-MCP-User",
    "run",
    "news_user/main.py"
  ]
}
```

---

### 6. **TaskManager-MCP**
Task management system with local JSON storage.

**Tools:**
- `task_add(description, due_date)` - Add a new task
- `task_list()` - List all tasks
- `task_delete(task_id)` - Delete a task
- `task_complete(task_id)` - Mark a task as completed

**Setup:**
- No external dependencies (uses local JSON file for storage)
- Dependencies: `fastmcp`

**Configuration:**
```json
"TaskManager-Tools": {
  "command": "uv",
  "args": [
    "--directory",
    "/absolute/path/to/Personal-Assistant-MCP/TaskManager-MCP",
    "run",
    "main.py"
  ]
}
```

---

### 7. **filesystem-MCP**
File system operations with security controls and .gitignore support.

**Tools:**
- `list_directory(path, recursive)` - List files and directories
- `read_file(path)` - Read file contents
- `write_file(path, content, create_dirs)` - Write/create files
- `create_directory(path, create_parents)` - Create directories
- `delete_path(path, recursive)` - Delete files or directories
- `copy_path(source_path, destination_path)` - Copy files/directories
- `move_path(source_path, destination_path)` - Move/rename files/directories
- `move_files_by_pattern(file_pattern, destination_folder, source_path)` - Move files matching a pattern
- `search_files(query, file_pattern)` - Search for text within files

**Setup:**
- Requires root directory path as command-line argument
- Respects `.gitignore` patterns
- Dependencies: `mcp-server`, `pathspec`

**Configuration:**
```json
"FileSystem-Tools": {
  "command": "uv",
  "args": [
    "--directory",
    "/absolute/path/to/Personal-Assistant-MCP/filesystem-MCP",
    "run",
    "main.py",
    "/absolute/path/to/allowed/directory"
  ]
}
```

---

## Setup Instructions

### Prerequisites

**Important:** Make sure you install the project in the root directory. Installing it in a path like `/onedrive/project` may cause issues. Save it to Desktop or a similar location instead.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CEN4090L-PROJECT-G26.git
cd CEN4090L-PROJECT-G26/Personal-Assistant-MCP
```

### 2. Install dependencies for each MCP server

For each MCP server you want to use, navigate to its directory and install dependencies:

```bash
cd <MCP-SERVER-NAME>
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .
```

### 3. Configure environment variables

Create `.env` files in the directories that require API keys:

- **Weather-Info**: `API_KEY=your_accuweather_key`
- **Stock-MCP**: `STOCK_API=your_alphavantage_key`
- **News-MCP**: `NEWS_API_KEY=your_newsapi_key`
- **Gmail-MCP**: Requires `credentials.json` for OAuth (see Google Cloud Console)

### 4. Configure Claude Desktop

1. Install Claude Desktop
2. Open Settings → Developer
3. Click "Edit Config" to open `mcp.config.json`
4. Add the MCP servers you want to use (see examples above)

**Complete Example Configuration:**

```json
{
  "mcpServers": {
    "Weather-Info": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/Personal-Assistant-MCP/Weather-Info",
        "run",
        "main.py"
      ]
    },
    "Gmail-Tools": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/Personal-Assistant-MCP/Gmail-MCP",
        "run",
        "main.py"
      ]
    },
    "Stock-MCP": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/Personal-Assistant-MCP/Stock-MCP",
        "run",
        "stockinfo.py"
      ]
    }
  }
}
```

### 5. Verify installation

In Claude Desktop, you should see the configured MCP servers running. You can also test them using:

```bash
mcp dev <path/to/main.py>
```

This allows you to see if the API calls are working correctly.

---

## Adding a New MCP Server

When adding a new MCP server that is not related to existing ones:

### 1. Initialize the project

```bash
cd Personal-Assistant-MCP
uv init <MCP-SERVER-NAME>
cd <MCP-SERVER-NAME>
uv venv
source .venv/bin/activate
```

### 2. Develop your MCP server

- Create your `main.py` with FastMCP server
- Define your tools using `@mcp.tool()` decorators
- Add dependencies to `pyproject.toml`

### 3. Install dependencies

```bash
uv pip install -e .
```

### 4. Add to Claude Desktop config

Add your new MCP server to `mcp.config.json`:

```json
{
  "mcpServers": {
    "Your-MCP-Name": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/Personal-Assistant-MCP/<MCP-SERVER-NAME>",
        "run",
        "main.py"
      ]
    }
  }
}
```

---

## Debugging

To debug an MCP server, use:

```bash
cd <MCP-SERVER-DIRECTORY>
mcp dev main.py
```

This will show API calls and any errors in real-time.

---

## License

MIT License - Copyright (c) 2025 Axel Reich

See [LICENSE](LICENSE) file for details.
