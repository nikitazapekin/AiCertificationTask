# Project Generator (Standalone)

Run project scaffolding via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `project-generator`
- **description:** `Scaffold project structure`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Scaffold NestJS project structure.

PROCESS:
1. Ask minimal setup questions
2. Apply smart defaults
3. Generate folder structure
4. Create ARCHITECTURE.md

GENERATES:
- Project folder structure
- NestJS module boundaries
- Empty controllers, services, repositories
- Minimal shared infrastructure (Config, Logger, Database, Health)
- Application bootstrap structure

DOES NOT GENERATE:
- Business logic or use cases
- Domain models or value objects
- Feature-specific functionality

ARCHITECTURE: STRICTLY LAYERED ONLY
Controller → Service → Repository

FORBIDDEN PATTERNS:
- DDD, CQRS, GraphQL, Event Sourcing

MODULE STRUCTURE:
modules/<name>/
├── <name>.module.ts
├── <name>.controller.ts
├── <name>.service.ts
├── <name>.repository.ts
├── dto/
└── entities/

STOP after generating project structure. Do not proceed to implementation.
```

**After sub-agent completes:** Report the generated structure to the user.
