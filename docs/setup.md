# Hướng dẫn thiết lập

## Yêu cầu

- Python 3.10+ cho các ví dụ 01–03
- Python 3.12+ cho `04-lab/mcp-client`
- `uv` cho Lab 04 (cài từ <https://docs.astral.sh/uv/>)

## Cài đặt ví dụ 01–03

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Chạy theo lộ trình

```bash
cd 02-mcp-basics && python weather_client.py

cd ../01-function-calling
export GEMINI_API_KEY="..."
python weather_function_calling.py

cd ../03-production
python auth_server.py       # terminal 1
python auth_client.py       # terminal 2
```

## Chạy Lab 04

Terminal 1:

```bash
cd 04-lab/mcp-server
uv sync
export WEATHERAPI_KEY="..."
uv run python weather.py
```

Terminal 2:

```bash
cd 04-lab/mcp-client
uv sync
printf 'GOOGLE_API_KEY=...\nMCP_SERVER_URL=http://localhost:8085/mcp\n' > .env
uv run adk web
```

Không commit file `.env`; hãy dùng `.env.example` làm mẫu.
