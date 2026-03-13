/**
 * Cross-platform npx launcher for MCP servers.
 * On Windows, `npx` is a .cmd file that can't be spawned directly
 * by Claude Code's stdio transport. This script bridges the gap.
 *
 * Usage in .mcp.json:
 *   "command": "node",
 *   "args": ["scripts/mcp-npx.js", "-y", "@some/mcp-package"]
 */
const { spawn } = require("child_process");

const npx = process.platform === "win32" ? "npx.cmd" : "npx";
const child = spawn(npx, process.argv.slice(2), {
  stdio: "inherit",
  shell: true,
});

child.on("exit", (code) => process.exit(code ?? 1));
