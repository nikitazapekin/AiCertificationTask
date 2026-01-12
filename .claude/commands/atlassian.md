# Atlassian Integration (Standalone)

Run the atlassian-skill to integrate with Jira and Confluence.

**Important:** This command runs the skill in isolation WITHOUT automatically triggering next steps.

## Input
$ARGUMENTS

## Instructions

Use the `atlassian-skill` to:

**Confluence Operations:**
- Fetch requirements from pages
- Extract acceptance criteria
- Create/update documentation

**Jira Operations:**
- Fetch issue details
- Update issue status
- Create new issues
- Add comments with evidence

Status transitions:
| Event | Jira Action |
|-------|-------------|
| Starting work | → "In Progress" |
| PR created | Add comment with PR link |
| Tests passing | Add comment with evidence |
| Complete | → "Done" |

Prerequisites:
- MCP tools for Atlassian (mcp__atlassian__*)
- If unavailable, inform user to configure Atlassian MCP server

**STOP after completing Atlassian operations.** Do not automatically proceed to other skills.
