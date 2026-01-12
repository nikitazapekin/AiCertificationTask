---
name: project-generator
description: Generate NestJS project structure with layered architecture (Controller/Service/Repository). Use for new projects, scaffolding, initial setup, or creating module structure. Triggers on "generate project", "scaffold", "create structure", "new project", "project setup", "init project". Creates minimal shared infrastructure and empty module stubs. Does NOT implement business logic or features.
---

# Project Generator

Generate clean, standardized NestJS project structures with layered architecture.

## Scope

**GENERATES:**
- Project folder structure
- NestJS module boundaries
- Empty controllers, services, repositories
- Minimal shared infrastructure (Config, Logger, Database, Health)
- Application bootstrap structure
- ARCHITECTURE.md documentation

**DOES NOT GENERATE:**
- Business logic or use cases
- Domain models or value objects
- Feature-specific functionality
- DTOs with fields (generates empty stubs only)

## Architecture Rules

**STRICTLY LAYERED ARCHITECTURE ONLY:**
```
Controller → Service → Repository
```

**FORBIDDEN PATTERNS:**
- DDD (Domain-Driven Design)
- CQRS (Command Query Responsibility Segregation)
- GraphQL
- Event Sourcing
- Feature-driven / Vertical slice architecture

## Workflow

```
1. ASK QUESTIONS → 2. INFER DEFAULTS → 3. GENERATE STRUCTURE → 4. CREATE DOCUMENTATION
```

### Step 1: Ask Minimal Questions

Ask only essential questions. Group into single message. **Use AskUserQuestion tool.**

```markdown
## Project Setup Questions

1. **Service purpose** (1-3 sentences): What does this service do?

2. **Service type:**
   - [ ] HTTP API
   - [ ] Background worker
   - [ ] Mixed (HTTP + Worker)

3. **Functional modules** (e.g., Users, Orders, Notifications):
   List the main modules needed.

4. **Database:**
   - [ ] PostgreSQL + TypeORM
   - [ ] PostgreSQL + Prisma
   - [ ] MySQL + TypeORM
   - [ ] MongoDB + Mongoose
   - [ ] No database

5. **External integrations:**
   - [ ] None
   - [ ] REST APIs (specify which)
   - [ ] Message broker (Kafka/RabbitMQ)
```

### Step 2: Apply Smart Defaults

If not specified, assume:
- Service type: HTTP API
- Database: PostgreSQL + TypeORM
- No external integrations
- No infrastructure-only modules
- No API versioning
- No rate limiting
- No feature flags

### Step 3: Generate Structure

See `references/structure-templates.md` for folder structures.

**Generation order:**
1. Core files (`main.ts`, `app.module.ts`)
2. Shared modules (`/shared`)
3. Feature modules (`/modules`)
4. Bootstrap files (`/bootstrap`)

### Step 4: Create Documentation

Generate `ARCHITECTURE.md` with:
- Project overview
- Module list with responsibilities
- Dependency diagram
- Development commands

## Shared Modules

Generate minimal, cross-cutting infrastructure only. See `references/shared-modules.md` for implementations.

| Module | Purpose | When to Include |
|--------|---------|-----------------|
| Config | Environment configuration | Always |
| Logger | Structured logging | Always |
| Errors | Global error handling | Always |
| Database | TypeORM/Prisma/Mongoose connection | If database selected |
| Health | Health check endpoints | Always for HTTP APIs |

**Rules:**
- Shared modules contain NO business logic
- Shared modules do NOT depend on feature modules
- All are reusable and generic

## Module Structure

Each feature module follows this pattern:

```
modules/<name>/
├── <name>.module.ts
├── <name>.controller.ts
├── <name>.service.ts
├── <name>.repository.ts    # Only if database is used
├── dto/
│   ├── create-<name>.dto.ts
│   └── update-<name>.dto.ts
└── entities/               # Only if database is used
    └── <name>.entity.ts
```

## Output Checklist

After generation, verify:
- [ ] All folders created
- [ ] All modules have `.module.ts`
- [ ] Controllers have basic CRUD routes (empty)
- [ ] Services have method stubs
- [ ] Repositories have TypeORM/Prisma setup
- [ ] `app.module.ts` imports all modules
- [ ] `ARCHITECTURE.md` is complete
