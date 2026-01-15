# Verification

Spawn verification agent to verify work before claiming completion.

## Input
$ARGUMENTS

## Instructions

Use the Task tool to spawn a sub-agent:
- **subagent_type:** `verification`
- **description:** `Verify work completion`
- **prompt:** `$ARGUMENTS`

The agent will use the verification skill and suggest next steps when done.
