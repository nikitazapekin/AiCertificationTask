---
name: architect
description: System architecture decisions for NestJS projects. Use when designing new features, choosing patterns, evaluating scalability/security, or making technology choices. Triggers on "design", "architect", "should I use", "which pattern", "scalability", "security design".
---

# Architect

## Overview

Make system architecture decisions for NestJS projects following Layered Architecture principles (Controller/Service/Repository).

## Decision Trees

### Where to Place New Code?

```
New functionality needed
        │
        ├── Business domain specific?
        │   └── YES → modules/<module>/
        │
        ├── Cross-cutting infrastructure?
        │   └── YES → shared/
        │
        └── External service integration?
            └── YES → shared/integrations/ or module-specific
```

### Which Pattern to Use?

```
Operation type?
        │
        ├── HTTP Request handling?
        │   └── Controller
        │
        ├── Business logic?
        │   └── Service
        │
        ├── Data access?
        │   └── Repository
        │
        └── Utility/helper function?
            └── Static utility or shared service
```

## Architecture Layers

```
┌─────────────────────────────────────────────────────────┐
│ Presentation Layer (Controllers, DTOs)                   │
├─────────────────────────────────────────────────────────┤
│ Service Layer (Business Logic)                           │
├─────────────────────────────────────────────────────────┤
│ Data Access Layer (Repositories, Entities)               │
└─────────────────────────────────────────────────────────┘
```

## Dependency Rules

```
✅ ALLOWED:
Controller → Service → Repository
Any layer → shared utilities

❌ NOT ALLOWED:
Repository → Service
Service → Controller
```

## Module Structure

```
modules/<module>/
├── <module>.module.ts
├── <module>.controller.ts
├── <module>.service.ts
├── <module>.repository.ts    # Only if database is used
├── dto/
│   ├── create-<module>.dto.ts
│   └── update-<module>.dto.ts
└── entities/                  # Only if database is used
    └── <module>.entity.ts
```

## Key Decisions

### Entity Relationships

| Relationship | Implementation | When |
|--------------|---------------|------|
| One-to-One | `@OneToOne` + FK | Rarely, usually merge entities |
| One-to-Many | `@OneToMany` + `@ManyToOne` | Common parent-child |
| Many-to-Many | `@ManyToMany` + junction table | Tags, categories |

### Transaction Boundaries

| Scenario | Transaction? | How |
|----------|-------------|-----|
| Single write | No (implicit) | Direct repository call |
| Multiple related writes | Yes | Service method with @Transaction |
| Read operation | No | Repository call |

### Security Considerations

- [ ] Authentication required?
- [ ] Authorization rules?
- [ ] Input validation?
- [ ] Rate limiting?
- [ ] Audit logging?
- [ ] Data encryption?

### Scalability Considerations

- [ ] Database indexing strategy?
- [ ] Caching opportunities?
- [ ] Async processing needed?
- [ ] Horizontal scaling requirements?

## Quick Reference

| Decision | Answer |
|----------|--------|
| New business entity | Entity + Repository + Service + Controller |
| External API integration | Shared integration service |
| Shared utilities | shared/ directory |
| Feature flag | Configuration service |
| Background job | Queue + worker pattern |
| Real-time updates | WebSockets or SSE |

---

## Final Output (MANDATORY)

**Before presenting next steps, you MUST write the architecture document to a file:**

1. Create the directory if it doesn't exist: `docs/analysis/architecture/`
2. Write the file: `docs/analysis/architecture/YYYY-MM-DD-<feature-name>-architecture.md`
3. Include:
   - Module placement decisions
   - Pattern choices with rationale
   - Entity relationships
   - Security considerations
   - Scalability considerations
   - Key architectural decisions table

**Example filename:** `docs/analysis/architecture/2024-01-15-payment-system-architecture.md`

This file preserves the architecture context so the conversation can be cleared before implementation.

---

## Next Steps

After architecture document is written to file, STOP and present these options:

**Next by flow:** `/api-designer [context]` - Design REST APIs based on the architecture.

**Alternatives:**
- `/writing-plans [context]` - Create implementation plan if APIs are already defined.
- `/coder [context]` - Start implementation if architecture is simple and clear.
