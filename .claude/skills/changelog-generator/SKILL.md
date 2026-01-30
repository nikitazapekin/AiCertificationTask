---
name: changelog-generator
description: Generate changelog entries based on git commits and code changes. Use before finishing-branch to document what changed in the current feature/fix. Triggers on "changelog", "generate changelog", "update changelog", "document changes".
---

# Changelog Generator

## Overview

Generate structured changelog entries based on git commits and code changes in the current branch. This skill analyzes commits since branching from main and creates properly formatted changelog entries.

## Generated File Naming Convention (MANDATORY)

**ANY additional documentation file created by this skill MUST be prefixed with `changelog-generator-`:**
- ✅ `changelog-generator-notes.md`
- ❌ `NOTES.md`

Standard project files (`CHANGELOG.md`) are exempt from this rule.

**Core principle:** Analyze commits → Categorize changes → Generate entry → Update CHANGELOG.md

**Announce at start:** "I'm using the changelog-generator skill to document changes."

## The Process

### Step 1: Determine Branch Context

```bash
# Get current branch name
git branch --show-current

# Find the base branch (main or master)
git merge-base HEAD main 2>/dev/null || git merge-base HEAD master 2>/dev/null

# Get commits since branching
git log --oneline $(git merge-base HEAD main)..HEAD 2>/dev/null || \
git log --oneline $(git merge-base HEAD master)..HEAD 2>/dev/null
```

### Step 2: Analyze Changes

```bash
# Get detailed diff summary
git diff --stat $(git merge-base HEAD main)..HEAD 2>/dev/null || \
git diff --stat $(git merge-base HEAD master)..HEAD 2>/dev/null

# List changed files
git diff --name-only $(git merge-base HEAD main)..HEAD 2>/dev/null || \
git diff --name-only $(git merge-base HEAD master)..HEAD 2>/dev/null
```

**Categorize each change:**

| Category | Description | Examples |
|----------|-------------|----------|
| Added | New features or capabilities | New endpoint, new component, new service |
| Changed | Modifications to existing behavior | Updated validation, changed API response |
| Fixed | Bug fixes | Resolved error, fixed edge case |
| Deprecated | Features marked for removal | Deprecated endpoint, deprecated method |
| Removed | Removed features | Deleted unused code, removed endpoint |
| Security | Security-related changes | Fixed vulnerability, added auth check |

### Step 3: Check Existing Changelog

```bash
# Check if CHANGELOG.md exists
ls -la CHANGELOG.md 2>/dev/null || echo "No CHANGELOG.md found"
```

**If no CHANGELOG.md exists, create one with header:**

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
```

### Step 4: Determine Version

**Ask user for version. Use AskUserQuestion tool:**

```
What version should this changelog entry use?

1. Patch (x.x.X) - Bug fixes, minor changes
2. Minor (x.X.0) - New features, backwards compatible
3. Major (X.0.0) - Breaking changes
4. Use [Unreleased] - Not ready for version yet
```

**If existing version in CHANGELOG.md:**
- Parse latest version and suggest increment
- Example: If `## [1.2.3]` exists, suggest `1.2.4` for patch

### Step 5: Generate Changelog Entry

**Entry format:**

```markdown
## [VERSION] - YYYY-MM-DD

### Added
- Description of new feature ([commit-hash])

### Changed
- Description of change ([commit-hash])

### Fixed
- Description of fix ([commit-hash])

### Deprecated
- Description of deprecated feature ([commit-hash])

### Removed
- Description of removed feature ([commit-hash])

### Security
- Description of security fix ([commit-hash])
```

**Writing guidelines:**
- Use imperative mood ("Add feature" not "Added feature")
- Be specific but concise
- Reference commit hashes in parentheses
- Group related changes
- Only include sections that have entries

### Step 6: Update CHANGELOG.md

**Insert new entry after the header, before previous entries:**

```bash
# Show current date for entry
date +%Y-%m-%d
```

**Confirm with user before writing. Use AskUserQuestion tool:**

```
Here's the generated changelog entry:

[Show formatted entry]

Should I add this to CHANGELOG.md?
1. Yes, add it
2. Let me edit first (show editable version)
3. Skip changelog update
```

### Step 7: Commit Changelog

**If user approved, commit the change:**

```bash
git add CHANGELOG.md
git commit -m "docs: update changelog for version X.X.X

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

## Entry Examples

### Feature Addition

```markdown
## [1.3.0] - 2024-01-15

### Added
- Add user authentication with JWT tokens (a1b2c3d)
- Add password reset flow via email (e4f5g6h)
- Add rate limiting for auth endpoints (i7j8k9l)
```

### Bug Fix

```markdown
## [1.2.1] - 2024-01-14

### Fixed
- Fix null pointer exception in user service (m1n2o3p)
- Fix incorrect date formatting in reports (q4r5s6t)
```

### Breaking Change

```markdown
## [2.0.0] - 2024-01-13

### Changed
- **BREAKING:** Change API response format from XML to JSON (u7v8w9x)
- **BREAKING:** Rename `/api/users` to `/api/v2/users` (y1z2a3b)

### Removed
- Remove deprecated `/api/v1/*` endpoints (c4d5e6f)
```

## Quick Reference

| Step | Action | Tool |
|------|--------|------|
| 1 | Get branch context | Bash (git) |
| 2 | Analyze changes | Bash (git diff) |
| 3 | Check existing changelog | Read/Bash |
| 4 | Determine version | AskUserQuestion |
| 5 | Generate entry | Format based on commits |
| 6 | Confirm with user | AskUserQuestion |
| 7 | Commit changelog | Bash (git) |

## Red Flags

**Never:**
- Generate changelog without analyzing actual commits
- Skip user confirmation before writing
- Use vague descriptions like "various fixes"
- Include commits that aren't related to current work
- Overwrite existing changelog entries

---

## Next Steps

After changelog is generated, STOP and present these options:

**Next by flow:** `/finishing-branch [context]` - Complete the branch (merge, PR, or cleanup).

**Alternatives:**
- `/code-reviewer [context]` - Review the changes one more time.
- `/docs-generator [context]` - Update other documentation (README, ADR).
