# Executing Plans

Spawn executing-plans agent to implement a written plan with batch execution.

## Input
$ARGUMENTS

## Instructions

Use the Task tool to spawn a sub-agent:
- **subagent_type:** `executing-plans`
- **description:** `Execute implementation plan`
- **prompt:** `$ARGUMENTS`

The agent will use the executing-plans skill and suggest next steps when done.
