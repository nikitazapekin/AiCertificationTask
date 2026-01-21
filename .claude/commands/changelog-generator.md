# Changelog Generator

Spawn changelog-generator agent to document changes before finishing branch.

## Input
$ARGUMENTS

## Instructions

Use the Task tool to spawn a sub-agent:
- **subagent_type:** `changelog-generator`
- **description:** `Generate changelog entry`
- **prompt:** `$ARGUMENTS`

The agent will use the changelog-generator skill and suggest next steps when done.
