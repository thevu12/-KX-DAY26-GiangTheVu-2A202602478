.PHONY: check test compile demo-mcp

check: compile test

compile:
	python3 -m compileall -q 01-function-calling 02-mcp-basics 03-production

test:
	python3 -m pytest -q

demo-mcp:
	cd 02-mcp-basics && python3 weather_client.py
