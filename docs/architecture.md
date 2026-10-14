# Kiến trúc dự án

Repo được chia thành hai lớp:

```text
examples/ (01–03)  ->  bài học độc lập, minh họa từng khái niệm
04-lab               ->  triển khai gần production
  mcp-server         ->  FastMCP + WeatherAPI
  mcp-client         ->  Google ADK + McpToolset
```

## Luồng Lab 04

```text
Browser -> ADK Web -> Weather Agent -> Streamable HTTP -> MCP Server -> WeatherAPI
```

Function Calling là khả năng của LLM để chọn tool. MCP là giao thức để agent
khám phá và gọi tool ở một server độc lập. Vì vậy hai lớp này bổ sung cho nhau.

## Nguyên tắc mở rộng

- Tool và tích hợp bên ngoài thuộc MCP server, không thuộc agent.
- Agent chỉ điều phối hội thoại và chọn tool.
- Cấu hình lấy từ environment variables.
- Mỗi service có `pyproject.toml`, lockfile và README riêng.
- Logic mới cần có test trước khi kết nối API thật.
