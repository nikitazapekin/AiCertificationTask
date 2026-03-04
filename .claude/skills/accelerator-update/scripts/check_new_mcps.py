#!/usr/bin/env python3
"""Detect newly added MCP servers by comparing old and new mcp-registry.json files."""

import json
import sys
from pathlib import Path


def check_new_mcps(old_path: str, new_path: str) -> None:
    old_registry = {}
    if Path(old_path).exists():
        with open(old_path, "r") as f:
            old_registry = json.load(f)

    new_registry = {}
    if Path(new_path).exists():
        with open(new_path, "r") as f:
            new_registry = json.load(f)

    new_servers = {k: v for k, v in new_registry.items() if k not in old_registry}

    if not new_servers:
        print("No new MCP servers in this update.")
        return

    print("New MCP servers added by this update:\n")
    for name, info in new_servers.items():
        desc = info.get("description", "No description")
        requires_auth = info.get("requiresAuth", False)
        setup = info.get("setupInstructions", "")
        env_vars = info.get("envVars", {})

        print(f"  {name} - {desc}")
        if requires_auth:
            print(f"    ⚠️  Requires configuration:")
        if setup:
            print(f"    Setup: {setup}")
        if env_vars:
            print(f"    Required env vars:")
            for var, hint in env_vars.items():
                print(f"      {var} - {hint}")
        print()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: check_new_mcps.py <old_registry> <new_registry>")
        sys.exit(1)

    check_new_mcps(sys.argv[1], sys.argv[2])
