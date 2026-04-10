---
name: browser-verify
description: Autonomous browser-based verification of UI changes. Use after any frontend code change to visually verify it works, catch console errors, detect broken interactions, and iterate fixes without asking the human. Triggers on "verify in browser", "check in browser", "does it look right", "visual check", "browser test", "open the app", "check the UI". Also use proactively after implementing or fixing any visible frontend change.
phase: execution
flow-next: code-reviewer
flow-alternatives: [coder-frontend, debugger]
related: [coder-frontend, verify, systematic-debugger, agent-browser]
---

# Browser Verify

Autonomous visual verification loop: make a change, observe it in the browser, decide if it works, fix if not, repeat until correct.

## Tools Available

### agent-browser CLI (DEFAULT)

Token-efficient CLI using accessibility tree with element refs (`@e1`, `@e2`). Run via Bash tool. Full reference: `.claude/skills/agent-browser/SKILL.md`.

**Quick reference:**
```bash
# Use batch for 2+ sequential commands (preferred over chaining)
agent-browser batch "open <url>" "snapshot -i"
agent-browser batch "open <url>" "screenshot"

# Individual commands (when you need to read output before next step)
agent-browser open <url>              # Open URL (waits for page load automatically)
agent-browser snapshot -i             # Get accessibility tree with refs
agent-browser screenshot              # Capture viewport
agent-browser screenshot --annotate   # Screenshot with numbered element labels
agent-browser click @e1               # Click element by ref
agent-browser fill @e3 "text"         # Fill input field
agent-browser get text @e2            # Get text content
agent-browser diff snapshot           # Compare current vs last snapshot
agent-browser console                 # View console messages
agent-browser errors                  # View page errors
agent-browser network requests        # Inspect network requests
agent-browser close                   # Close browser
```

**Critical rules:**
- Refs become stale after ANY navigation or DOM change. Always `agent-browser snapshot -i` before interacting after a page change.
- `open` already waits for `load` event — no need for extra `wait` after navigation in most cases.
- **Avoid `wait --load networkidle`** — it hangs on sites with analytics, ads, or websockets. Use `wait 2000` or `wait <selector>` instead.

### Playwright MCP (ESCALATION ONLY)

Full browser control via MCP. Use only when agent-browser can't diagnose the issue.

- `mcp__playwright__browser_navigate` — navigate to URL
- `mcp__playwright__browser_click` — click element by selector
- `mcp__playwright__browser_screenshot` — capture screenshot
- `mcp__playwright__browser_console_messages` — read console errors/warnings
- `mcp__playwright__browser_network_requests` — inspect failed API calls
- `mcp__playwright__browser_evaluate` — run JS in page context

## Decision: Which Tool

```
Start with agent-browser (always)
  |
  Can you see the problem? ──yes──> Fix it, re-verify with agent-browser
  |
  no
  |
  Need console logs, network, or JS eval? ──yes──> Try agent-browser first:
  |                                                  console / errors / network requests / eval
  |                                                  |
  |                                                  Still not enough? → Switch to Playwright MCP
  |                                                  |
  no                                                 Fix + re-verify
  |
  Take screenshot, compare to expectation
```

**Switch to Playwright MCP when:**
- agent-browser `console`/`errors`/`network` commands don't provide enough detail
- Interaction sequence is complex (drag, hover states, focus traps)
- Need to run complex JS assertions in page context

**Stay on agent-browser when:**
- Checking layout, text content, visibility
- Clicking buttons and verifying navigation
- Reading form states via accessibility tree
- Simple before/after visual comparison
- Checking console errors (`agent-browser console`) or network issues (`agent-browser network requests`)

## Verification Loop

### 1. Pre-check
```
Determine the app URL (ask user if unknown, default http://localhost:3000)
Determine what to verify (from the change just made)
Define success criteria: what should be visible/interactive/absent
```

### 2. Observe
```bash
agent-browser batch "open http://localhost:3000/relevant-page" "snapshot -i"
# If visual check needed:
agent-browser screenshot
```
Compare actual state against success criteria.

### 3. Decide
```
PASS → Report success with evidence (snapshot excerpt or screenshot). Stop.
FAIL → Identify the discrepancy. Proceed to step 4.
UNCLEAR → Take screenshot + snapshot for more data. Re-decide.
```

### 4. Fix
```
Make the code fix based on observed evidence
Wait for hot-reload (~2s) or trigger rebuild
Re-verify (refs are now stale):
  agent-browser batch "open http://localhost:3000/relevant-page" "snapshot -i"
Return to step 2
```

### 5. Circuit Breaker
```
After 3 failed fix attempts on the SAME issue:
  → Stop. Report what was tried, what was observed, what remains broken.
  → Ask the user for guidance.
Never loop more than 3 times without progress.
```

## Token Management

- **Prefer `snapshot -i` over `screenshot`** for content/structure checks — far fewer tokens
- **Use `batch`** to combine sequential commands into a single tool call
- **Use `diff snapshot`** after a fix to see exactly what changed instead of re-reading the whole page
- **Use screenshots only when** layout/styling/visual appearance matters
- **Use `get text @eN`** on specific elements instead of re-snapshotting the whole page
- **Close browser** (`agent-browser close`) when done or before switching to Playwright MCP
- **One tool at a time** — don't run agent-browser and Playwright simultaneously

## Patterns

### Quick visual check (most common)
```bash
agent-browser batch "open http://localhost:3000" "snapshot -i"
# Verify expected elements present in the accessibility tree
# Report PASS/FAIL
agent-browser close
```

### Style/layout verification
```bash
agent-browser batch "open http://localhost:3000/page" "screenshot --annotate"
# Compare against design intent visually
# Report PASS/FAIL
agent-browser close
```

### Interactive flow verification
```bash
agent-browser batch "open http://localhost:3000/login" "snapshot -i"
# Read snapshot to get refs, then interact
agent-browser batch "fill @e3 \"user@example.com\"" "fill @e5 \"password123\"" "click @e7" "wait 2000"
agent-browser snapshot -i                    # Re-snapshot — refs are stale after navigation
# Verify redirected to dashboard, expected content visible
agent-browser close
```

### Verify a fix with diff
```bash
agent-browser batch "open http://localhost:3000/page" "snapshot -i"  # Baseline before fix
# ... make the code fix, wait ~2s for hot-reload ...
agent-browser batch "open http://localhost:3000/page" "snapshot -i"
agent-browser diff snapshot                  # See exactly what changed
agent-browser close
```

### Responsive testing
```bash
agent-browser batch "open http://localhost:3000/page" "set viewport 375 812" "screenshot mobile.png"
agent-browser batch "set viewport 1920 1080" "screenshot desktop.png"
# Compare mobile vs desktop layouts
agent-browser close
```

### Debug with console/network (before escalating to Playwright)
```bash
agent-browser batch "open http://localhost:3000/page" "snapshot -i"
agent-browser console                        # Check for JS errors
agent-browser errors                         # Check for page errors
agent-browser network requests --status 4xx  # Check for failed API calls
agent-browser network requests --status 5xx  # Check for server errors
# Root cause identified → fix → re-verify
agent-browser close
```

### Debug failing interaction (escalate to Playwright)
```bash
agent-browser close                          # Close agent-browser first
```
Then use Playwright MCP tools:
```
mcp__playwright__browser_navigate → reproduce the flow
mcp__playwright__browser_console_messages → check for errors
mcp__playwright__browser_network_requests → check for failed API calls
mcp__playwright__browser_evaluate → inspect DOM state
```
Root cause identified → fix → re-verify with agent-browser.

## Rules

- **Always verify after fixing** — never assume a code change worked
- **Always re-snapshot after DOM changes** — refs go stale on any navigation or interaction that changes the page
- **Evidence over assumption** — report what you SAW, not what should happen
- **One issue at a time** — fix the most visible problem first, then re-verify
- **Don't ask the human** unless the circuit breaker triggers or you need the app URL
- **Hot-reload awareness** — after saving a file, wait ~2s before checking the browser
- **Close before switching** — close agent-browser before using Playwright MCP and vice versa
- **Avoid networkidle** — use `wait 2000` or `wait <selector>` instead of `wait --load networkidle`

---

## Next Steps

After verification is complete, STOP and present these options:

**Next by flow:** [[/code-reviewer]] `[context]` - Review the code for quality and issues. See [[moc-execution]] for phase context.

**Alternatives:**
- [[/coder-frontend]] `[context]` - Continue frontend implementation if more changes needed.
- [[/debugger]] `[context]` - Deep investigation if browser-verify couldn't resolve the issue.
