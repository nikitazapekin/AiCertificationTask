# Claude Code Hooks Documentation

## Configured Hooks

This project has several hooks configured to enhance the development workflow.

### 1. SessionStart Hook

**Triggers**: When starting a new Claude Code session

**Purpose**: Welcome message and timestamp

**Command**:
```bash
echo '🚀 Claude Code session started' && date
```

**Output**: Displays session start time

---

### 2. Notification Hook ⭐

**Triggers**: When Claude sends notifications (permission requests, waiting for input)

**Purpose**: Desktop notifications (macOS) or console alerts

**Command**:
```bash
osascript -e 'display notification "Claude needs your attention" with title "Claude Code" sound name "default"' 2>/dev/null || echo '🔔 Claude Code notification'
```

**Features**:
- macOS: Shows native notification with sound
- Other OS: Falls back to console message
- Helps you know when Claude needs interaction

**Customization**:
```bash
# Change notification sound (macOS)
osascript -e 'display notification "..." sound name "Basso"'
# Available sounds: Basso, Blow, Bottle, Frog, Funk, Glass, Hero, Morse, Ping, Pop, Purr, Sosumi, Submarine, Tink

# Add custom message
osascript -e 'display notification "Custom message here" with title "Title" subtitle "Subtitle"'

# Linux (using notify-send)
notify-send "Claude Code" "Claude needs your attention"

# Windows (PowerShell)
powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show('Message')"
```

---

### 3. Stop Hook

**Triggers**: When Claude finishes responding

**Purpose**: Completion timestamp

**Command**:
```bash
echo '✅ Response completed at' && date
```

**Output**: Shows when Claude finished processing

---

### 4. PreToolUse Hooks

#### Bash Command Hook

**Triggers**: Before executing any Bash command

**Purpose**: Visual feedback that command is about to run

**Command**:
```bash
echo '🔧 Executing bash command...'
```

#### File Modification Hook

**Triggers**: Before Edit or Write operations

**Purpose**: Alert that file will be modified

**Command**:
```bash
echo '📝 Modifying file...'
```

---

### 5. PostToolUse Hook

**Triggers**: After successful Write or Edit operations

**Purpose**: Confirmation that file was saved

**Command**:
```bash
echo '✨ File saved successfully'
```

---

## Advanced Hook Examples

### Auto-lint TypeScript Files

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'FILE=$(echo \"$0\" | jq -r \".tool_input.file_path // empty\"); if [[ \"$FILE\" =~ \\.(ts|tsx)$ ]]; then npx eslint --fix \"$FILE\" 2>/dev/null || true; fi'",
            "timeout": 15000
          }
        ]
      }
    ]
  }
}
```

### Run Tests After Modifying Test Files

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'FILE=$(echo \"$0\" | jq -r \".tool_input.file_path // empty\"); if [[ \"$FILE\" =~ \\.spec\\.ts$ ]]; then npx nx test $(dirname \"$FILE\" | grep -oP \"(?<=libs/)[^/]+(?=/)\") --testFile=$(basename \"$FILE\") 2>/dev/null || true; fi'",
            "timeout": 30000
          }
        ]
      }
    ]
  }
}
```

### Security Check: Block .env Modifications

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'FILE=$(echo \"$0\" | jq -r \".tool_input.file_path // empty\"); if [[ \"$FILE\" =~ \\.env ]]; then echo \"❌ Cannot modify .env files\" && exit 2; fi'",
            "timeout": 1000
          }
        ]
      }
    ]
  }
}
```

### Git Auto-commit After File Changes

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'FILE=$(echo \"$0\" | jq -r \".tool_input.file_path // empty\"); git add \"$FILE\" && git commit -m \"Auto-commit: $(basename \"$FILE\")\" 2>/dev/null || true'",
            "timeout": 5000
          }
        ]
      }
    ]
  }
}
```

### Log All Tool Usage

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'echo \"$(date): Tool used\" >> ~/.claude/tool-usage.log'",
            "timeout": 1000
          }
        ]
      }
    ]
  }
}
```

### Backup Files Before Modification

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'FILE=$(echo \"$0\" | jq -r \".tool_input.file_path // empty\"); if [ -f \"$FILE\" ]; then cp \"$FILE\" \"$FILE.backup.$(date +%s)\"; fi'",
            "timeout": 2000
          }
        ]
      }
    ]
  }
}
```

## Hook Environment Variables

Hooks have access to special environment variables:

- `CLAUDE_PROJECT_DIR` - Current project directory
- `CLAUDE_FILE_PATHS` - Files being modified (for some hooks)
- `CLAUDE_TOOL_INPUT` - Tool parameters (JSON format)
- `CLAUDE_TOOL_NAME` - Name of the tool being used

Access via stdin (JSON):
```bash
echo "$0" | jq -r '.tool_input.file_path'
echo "$0" | jq -r '.tool_input.command'
```

## Hook Return Codes

- `0` - Success, continue
- `1` - Failure, but continue (logged as warning)
- `2` - Failure, block operation (shows error to user)

Example blocking hook:
```bash
# Block if file contains sensitive data
if grep -q "PASSWORD" "$FILE"; then
  echo "❌ File contains sensitive data!"
  exit 2  # Block the operation
fi
```

## Debugging Hooks

### Test hook manually:
```bash
# Simulate hook input
echo '{"tool_input":{"file_path":"test.ts"}}' | bash -c 'FILE=$(echo "$0" | jq -r ".tool_input.file_path"); echo "File: $FILE"'
```

### Enable hook debugging:
```bash
# Add to hook command
set -x  # Enable bash debug mode
```

### Check hook logs:
```bash
# macOS
tail -f /var/log/system.log | grep claude

# Linux
journalctl -f | grep claude
```

## Performance Tips

1. **Keep hooks fast** (< 100ms for PreToolUse)
2. **Use `|| true`** to prevent failures from blocking
3. **Set appropriate timeouts** (default 5000ms)
4. **Run expensive operations async** (background with `&`)
5. **Cache results** when possible

## Best Practices

1. **Test hooks before committing** to team settings
2. **Document all hooks** in this README
3. **Use team settings** for required hooks
4. **Use local settings** for personal preferences
5. **Avoid destructive hooks** in team settings
6. **Handle errors gracefully** (don't block on warnings)
7. **Respect timeout limits**
8. **Log important operations**

## Team vs Personal Hooks

**Team hooks** (`.claude/settings.json`):
- Non-intrusive notifications
- Logging and auditing
- Security checks
- Simple feedback messages

**Personal hooks** (`.claude/settings.local.json`):
- Auto-formatting (personal preference)
- Custom notifications (desktop alerts)
- Development tools
- Experimental features

## Disabling Hooks

### Disable all hooks temporarily:
```json
{
  "hooks": {}
}
```

### Disable specific hook type:
```json
{
  "hooks": {
    "PostToolUse": []
  }
}
```

### Override team hooks locally:
Add to `.claude/settings.local.json`:
```json
{
  "hooks": {
    "Notification": []  // Disable notifications
  }
}
```

## References

- [Claude Code Hooks Documentation](https://docs.anthropic.com/claude-code)
- [jq Manual](https://stedolan.github.io/jq/manual/)
- [Bash Exit Codes](https://tldp.org/LDP/abs/html/exitcodes.html)
