# Atlassian Integration (Standalone)

Run Atlassian operations via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `atlassian-skill`
- **description:** `Atlassian integration`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Integrate with Jira and Confluence.

CONFLUENCE OPERATIONS:
- Fetch requirements from pages
- Extract acceptance criteria
- Create/update documentation

JIRA OPERATIONS:
- Fetch issue details
- Update issue status
- Create new issues
- Add comments with evidence

STATUS TRANSITIONS:
| Event | Jira Action |
|-------|-------------|
| Starting work | → "In Progress" |
| PR created | Add comment with PR link |
| Tests passing | Add comment with evidence |
| Complete | → "Done" |

PREREQUISITES:
- MCP tools for Atlassian (mcp__atlassian__*)
- If unavailable, inform user to configure Atlassian MCP server

STOP after completing Atlassian operations. Do not proceed to other skills.
```

**After sub-agent completes:** Report the Atlassian actions to the user.
