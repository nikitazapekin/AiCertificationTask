# Documentation Generator (Standalone)

Run documentation generation via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `documentation-generator`
- **description:** `Generate documentation`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Create and maintain project documentation.

DOCUMENTATION TYPES:
1. Library README (overview, usage, API reference)
2. Domain README (architecture, endpoints, services)
3. ADR (Architecture Decision Record)
4. Changelog entry
5. JSDoc comments

DOCUMENTATION LOCATIONS:
- libs/<name>/README.md - Library docs
- docs/adrs/ - Architecture decisions
- CHANGELOG.md - Version history
- CLAUDE.md - AI context patterns

CHECKLIST FOR NEW FEATURE:
- [ ] README updated
- [ ] ADR if architectural decision
- [ ] Changelog entry
- [ ] JSDoc for public functions

STOP after completing documentation. Do not proceed to reflection or other skills.
```

**After sub-agent completes:** Report the documentation updates to the user.
