"""Kiểm tra các ví dụ mock, không gọi mạng hay cần API key."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).parents[1]


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_function_calling_mock_weather():
    module = load_module(
        ROOT / "01-function-calling" / "weather_function_calling.py",
        "function_calling_weather",
    )
    result = module.get_weather("Hà Nội")
    assert "Hà Nội" in result
    assert "29°C" in result
