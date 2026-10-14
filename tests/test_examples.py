"""Các test không cần gọi LLM hay WeatherAPI thật."""

import json
from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_registry_has_servers_and_tools():
    registry = json.loads((ROOT / "03-production" / "registry.json").read_text())
    assert registry["servers"]
    assert registry["tools"]
    for tool in registry["tools"].values():
        assert tool["server"] in registry["servers"]


def test_required_readmes_exist():
    for path in (
        "README.md",
        "01-function-calling/README.md",
        "02-mcp-basics/README.md",
        "03-production/README.md",
        "04-lab/README.md",
        "04-lab/mcp-client/README.md",
    ):
        assert (ROOT / path).is_file(), path
