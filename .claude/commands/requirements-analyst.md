# Requirements Analyst (Standalone)

Run the requirements-analyst skill to analyze and decompose requirements.

**Important:** This command runs the skill in isolation WITHOUT automatically triggering next steps (brainstorming, architect, etc.).

## Input
$ARGUMENTS

## Instructions

Use the `requirements-analyst` skill to:
1. Parse requirements from the provided input (Confluence page, spec, user request)
2. Decompose into actionable tasks
3. Identify acceptance criteria
4. Map to technical components

Output a structured requirements document with:
- Functional requirements
- Non-functional requirements
- Business rules
- Task breakdown
- Gap analysis

**STOP after completing the requirements analysis.** Do not automatically proceed to brainstorming or other skills.
