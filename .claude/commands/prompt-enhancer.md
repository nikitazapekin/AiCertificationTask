---
spawns: prompt-enhancer-agent
phase: utility
flow-next: null
flow-alternatives: [brainstorm, coder]
---

# Prompt Enhancer

Spawn prompt enhancer agent to craft, audit, or optimize prompts.

## Input
$ARGUMENTS

## Instructions

Use the Task tool to spawn a sub-agent:
- **subagent_type:** `prompt-enhancer`
- **description:** `Prompt engineering`
- **prompt:** `$ARGUMENTS`

The agent will use the prompt engineering skill and suggest next steps when done.
