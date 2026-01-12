# Project Generator (Standalone)

Run the project-generator skill to scaffold NestJS project structure.

**Important:** This command runs the skill in isolation WITHOUT automatically triggering next steps.

## Input
$ARGUMENTS

## Instructions

Use the `project-generator` skill to:
1. Ask minimal setup questions
2. Apply smart defaults
3. Generate folder structure
4. Create ARCHITECTURE.md

**GENERATES:**
- Project folder structure
- NestJS module boundaries
- Empty controllers, services, repositories
- Minimal shared infrastructure (Config, Logger, Database, Health)
- Application bootstrap structure

**DOES NOT GENERATE:**
- Business logic or use cases
- Domain models or value objects
- Feature-specific functionality

Architecture: **STRICTLY LAYERED ONLY**
```
Controller → Service → Repository
```

Forbidden patterns:
- DDD, CQRS, GraphQL, Event Sourcing

Module structure:
```
modules/<name>/
├── <name>.module.ts
├── <name>.controller.ts
├── <name>.service.ts
├── <name>.repository.ts
├── dto/
└── entities/
```

**STOP after generating project structure.** Do not automatically proceed to implementation.
