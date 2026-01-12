# Architect (Standalone)

Run the architect skill to make system architecture decisions.

**Important:** This command runs the skill in isolation WITHOUT automatically triggering next steps (api-designer, coder, etc.).

## Input
$ARGUMENTS

## Instructions

Use the `architect` skill to:
1. Determine where to place new code (module, shared, integration)
2. Select appropriate patterns (controller, service, repository)
3. Define architecture layers and dependencies
4. Make technology decisions
5. Consider security and scalability

Provide decisions on:
- Layer placement
- Module structure
- Entity relationships
- Transaction boundaries
- Component boundaries

**STOP after completing architecture decisions.** Do not automatically proceed to API design or implementation.
