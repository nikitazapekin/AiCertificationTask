# Claude Code Hooks Documentation

## Notification Hook

**Triggers**: When Claude sends notifications (permission requests, waiting for input)

**Purpose**: Desktop notification so you know when Claude needs interaction.

### Setup

In `.claude/settings.json` currently configured the **WSL (or Windows PowerShell)** variant.
To switch OS — replace the `"command"` value in the `Notification` hook with the appropriate command below.

---

### WSL (or Windows PowerShell) — current active

Uses Windows Toast notification via PowerShell:

```json
{
  "hooks": {
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "powershell.exe -Command \"[void][System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms'); $n = New-Object System.Windows.Forms.NotifyIcon; $n.Icon = [System.Drawing.SystemIcons]::Information; $n.Visible = $true; $n.ShowBalloonTip(3000, 'Claude Code', 'Claude needs your attention', 'Info')\" 2>/dev/null || echo '🔔 Claude Code notification'",
            "timeout": 5000
          }
        ]
      }
    ]
  }
}
```

---

### macOS

Uses native macOS notification with sound:

```json
{
  "hooks": {
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude needs your attention\" with title \"Claude Code\" sound name \"default\"'",
            "timeout": 2000
          }
        ]
      }
    ]
  }
}
```

Available sounds: Basso, Blow, Bottle, Frog, Funk, Glass, Hero, Morse, Ping, Pop, Purr, Sosumi, Submarine, Tink.

---

### Ubuntu / Linux

Uses `notify-send` (part of `libnotify-bin`):

```json
{
  "hooks": {
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "notify-send -u normal -t 3000 'Claude Code' 'Claude needs your attention' 2>/dev/null || echo '🔔 Claude Code notification'",
            "timeout": 2000
          }
        ]
      }
    ]
  }
}
```

Install if missing:
```bash
sudo apt install libnotify-bin
```

---

## Hook Reference

### Return Codes

- `0` — Success, continue
- `1` — Failure, but continue (logged as warning)
- `2` — Failure, block operation (shows error to user)

### Environment Variables

- `CLAUDE_PROJECT_DIR` — Current project directory
- `CLAUDE_FILE_PATHS` — Files being modified
- `CLAUDE_TOOL_INPUT` — Tool parameters (JSON)
- `CLAUDE_TOOL_NAME` — Name of the tool being used

### Hook Types

| Hook | When it fires |
|------|--------------|
| `SessionStart` | New Claude Code session |
| `Notification` | Claude needs user attention |
| `Stop` | Claude finishes responding |
| `PreToolUse` | Before a tool executes |
| `PostToolUse` | After a tool executes |

### Personal Hooks

Use `.claude/settings.local.json` for personal hooks that shouldn't be shared with the team.

## References

- [Claude Code Hooks Documentation](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [jq Manual](https://stedolan.github.io/jq/manual/)
