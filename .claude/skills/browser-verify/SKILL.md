---
name: browser-verify
description: Autonomous browser-based verification of UI changes. Use after any frontend code change to visually verify it works, catch console errors, detect broken interactions, and iterate fixes without asking the human. Triggers on "verify in browser", "check in browser", "does it look right", "visual check", "browser test", "open the app", "check the UI". Also use proactively after implementing or fixing any visible frontend change.
phase: execution
flow-next: code-reviewer
flow-alternatives: [coder-frontend, debugger]
related: [coder-frontend, verify, systematic-debugger]
---

# Browser Verify

Autonomous visual verification loop: make a change, observe it in the browser, decide if it works, fix if not, repeat until correct.

## MCP Tools Available

Two browser MCPs are configured in `.mcp.json` — both available via npx with zero setup:

### agent-browser (DEFAULT)
Token-efficient. Returns accessibility tree with element refs. Best for fast checks.
- `agent_browser_click`, `agent_browser_type`, `agent_browser_navigate`
- `agent_browser_get_accessibility_tree` — structured page state
- `agent_browser_screenshot` — visual snapshot
- `agent_browser_wait`

### Playwright MCP (ESCALATION ONLY)
Full browser control. Use only when agent-browser can't diagnose the issue.
- `browser_navigate`, `browser_click`, `browser_type`, `browser_screenshot`
- `browser_console_messages` — read console errors/warnings
- `browser_network_requests` — inspect failed API calls
- `browser_evaluate` — run JS in page context

## Decision: Which MCP

```
Start with agent-browser (always)
  |
  Can you see the problem? ──yes──> Fix it, re-verify with agent-browser
  |
  no
  |
  Need console logs, network, or JS eval? ──yes──> Switch to Playwright
  |                                                  |
  no                                                 Fix + re-verify
  |
  Take screenshot, compare to expectation
```

**Switch to Playwright when:**
- Console errors suspected but not visible in UI
- API calls failing silently
- Need to inspect DOM state or run JS assertions
- Interaction sequence is complex (drag, hover states, focus traps)

**Stay on agent-browser when:**
- Checking layout, text content, visibility
- Clicking buttons and verifying navigation
- Reading form states via accessibility tree
- Simple before/after visual comparison

## Verification Loop

### 1. Pre-check
```
Determine the app URL (ask user if unknown, default http://localhost:3000)
Determine what to verify (from the change just made)
Define success criteria: what should be visible/interactive/absent
```

### 2. Observe
```
Navigate to the relevant page
Take screenshot OR read accessibility tree
Compare actual state against success criteria
```

### 3. Decide
```
PASS → Report success with evidence (screenshot or tree excerpt). Stop.
FAIL → Identify the discrepancy. Proceed to step 4.
UNCLEAR → Take screenshot + accessibility tree for more data. Re-decide.
```

### 4. Fix
```
Make the code fix based on observed evidence
Wait for hot-reload (~2s) or trigger rebuild
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

Browser tools are expensive. Minimize token burn:

- **Prefer accessibility tree over screenshots** for content/structure checks — far fewer tokens
- **Use screenshots only when** layout/styling/visual appearance matters
- **Never take full-page screenshots** if you can target a specific element or viewport section
- **Don't re-read the whole page** after a small change — navigate to the specific area
- **Close browser tabs** when switching between Playwright and agent-browser to avoid state conflicts

## Patterns

### Quick visual check (most common)
```
1. agent_browser_navigate → app URL
2. agent_browser_get_accessibility_tree → verify expected elements present
3. Report PASS/FAIL
```

### Style/layout verification
```
1. agent_browser_navigate → app URL
2. agent_browser_screenshot → visual check
3. Compare against design intent
4. Report PASS/FAIL
```

### Debug failing interaction
```
1. agent_browser_navigate → reproduce the flow
2. agent_browser_click / agent_browser_type → trigger the interaction
3. If unexpected result → escalate to Playwright:
   a. browser_console_messages → check for errors
   b. browser_network_requests → check for failed calls
   c. browser_evaluate → inspect DOM state
4. Root cause identified → fix → re-verify with agent-browser
```

### Post-fix regression check
```
1. Fix the code
2. Wait 2s for hot-reload
3. agent_browser_navigate (force refresh)
4. Verify the fix AND check nothing else broke on the same page
```

## Rules

- **Always verify after fixing** — never assume a code change worked
- **Evidence over assumption** — report what you SAW, not what should happen
- **One issue at a time** — fix the most visible problem first, then re-verify
- **Don't ask the human** unless the circuit breaker triggers or you need the app URL
- **Hot-reload awareness** — after saving a file, wait ~2s before checking the browser
- **State conflicts** — if switching from agent-browser to Playwright, navigate fresh; don't assume the page state carried over
