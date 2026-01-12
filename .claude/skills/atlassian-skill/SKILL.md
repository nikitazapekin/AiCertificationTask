---
name: atlassian-skill
description: Integrate with Atlassian tools (Jira, Confluence) for requirement tracking and documentation. Use when fetching requirements from Confluence, creating/updating Jira issues, or syncing work status. Triggers on "Jira", "Confluence", "requirement", "ticket", "issue", "sprint".
---

# Atlassian Skill

## Overview

Integrate with Atlassian tools (Jira, Confluence) for requirement tracking, issue management, and documentation syncing.

**Core principle:** Keep Atlassian tools as source of truth for requirements and status.

**Announce at start:** "I'm using the atlassian-skill to [fetch requirements from Confluence / update Jira status / create ticket]."

## Prerequisites

This skill requires MCP tools for Atlassian integration:
- `mcp__atlassian__confluence_*` - Confluence operations
- `mcp__atlassian__jira_*` - Jira operations

If these tools are not available, inform the user to configure the Atlassian MCP server.

## Confluence Operations

### Fetch Requirements

**When:** Starting new feature, need to understand requirements

```
1. Get page content by ID or title
2. Parse requirements from page content
3. Extract acceptance criteria
4. Identify linked resources
```

**Key information to extract:**
- User stories
- Acceptance criteria
- Technical requirements
- Linked Jira issues
- Related documentation

### Create Documentation

**When:** Feature complete, need to document

```markdown
## Page Structure

### Feature: [Name]

**Status:** [In Progress | Complete]
**Related Issues:** [PROJ-123, PROJ-124]

### Overview
[Feature description]

### Technical Details
[Implementation details]

### API Endpoints
[If applicable]

### Usage
[How to use the feature]
```

## Jira Operations

### Fetch Issue Details

**When:** Need to understand ticket requirements

```
1. Get issue by key (PROJ-123)
2. Extract description, acceptance criteria
3. Get linked issues and epics
4. Check current status and assignee
```

### Update Issue Status

**When:** Task status changes

| Event | Jira Action |
|-------|-------------|
| Starting work | Transition to "In Progress" |
| PR created | Add comment with PR link |
| Tests passing | Add comment with evidence |
| Complete | Transition to "Done" |

### Create Issues

**When:** Discovered subtasks or bugs during development

```
Issue Type: [Bug | Task | Subtask]
Summary: [Brief description]
Description:
- Context: [Why this is needed]
- Acceptance Criteria: [When is it done]
- Technical Notes: [Implementation hints]
Parent: [Link to parent issue if subtask]
Labels: [Relevant labels]
```

## Integration Workflows

### Workflow 1: Start Feature from Confluence

```
1. User provides Confluence page link/ID
2. Fetch page content
3. Parse requirements
4. Pass to requirements-analyst skill
5. Create implementation plan
6. Create/link Jira issues for tasks
```

### Workflow 2: Update Progress

```
1. Task completed
2. Update Jira issue status
3. Add comment with:
   - What was implemented
   - Test evidence
   - PR link if applicable
```

### Workflow 3: Document Completion

```
1. Feature complete
2. Update Confluence page:
   - Add implementation details
   - Link to code/PRs
   - Add usage documentation
3. Update Jira:
   - Close related issues
   - Add final comments
```

## Best Practices

### Confluence
- Keep technical docs in sync with code
- Link to source code where possible
- Update pages after significant changes
- Use templates for consistency

### Jira
- Update status promptly
- Add meaningful comments (not noise)
- Link related issues
- Use appropriate issue types

## Error Handling

**Use AskUserQuestion tool for all error handling that requires user input.**

| Error | Action |
|-------|--------|
| Page not found | Ask user for correct page ID/title |
| Permission denied | Inform user, ask for access |
| Issue not found | Verify issue key with user |
| Transition failed | Check available transitions, inform user |

## Quick Reference

### Confluence Page Fetch
```
mcp__atlassian__confluence_get_page(pageId: "123456")
mcp__atlassian__confluence_search(query: "feature name")
```

### Jira Issue Operations
```
mcp__atlassian__jira_get_issue(issueKey: "PROJ-123")
mcp__atlassian__jira_update_issue(issueKey: "PROJ-123", status: "In Progress")
mcp__atlassian__jira_add_comment(issueKey: "PROJ-123", body: "Comment text")
mcp__atlassian__jira_create_issue(project: "PROJ", issueType: "Task", summary: "...")
```

## Integration

**Called by:**
- `requirements-analyst` - To fetch requirements from Confluence
- `new-feature` - For requirement tracking
- `finishing-branch` - To update status on completion

**Pairs with:**
- `requirements-analyst` - Parse fetched requirements
- `documentation-generator` - Sync docs to Confluence
