## Hybrid Approach: Index + Modular Files

**Neither extreme is ideal.** Use a **manifest file + focused spec files**.

```
specs/
├── MANIFEST.md          # Index + project overview (always read first)
├── architecture.md      # For architect agent
├── api-spec.md          # For api-designer agent
├── frontend-spec.md     # For frontend-designer agent
└── implementation.md    # Generated, for docs-generator
```

---

## MANIFEST.md Structure

```markdown
# Project: {Name}
{2-3 sentence core purpose}

## Specs Index
| File | Purpose | Depends On |
|------|---------|------------|
| architecture.md | System design, components, data flow | - |
| api-spec.md | Endpoints, schemas, auth | architecture |
| frontend-spec.md | Pages, components, state | architecture, api-spec |

## Key Decisions
- Auth: JWT with refresh tokens
- DB: PostgreSQL
- Frontend: React + TypeScript
```

---

## Why This Works Better for AI

| Factor | One Big File | Separate + Manifest |
|--------|--------------|---------------------|
| Token cost per agent | High (reads everything) | Low (reads only relevant) |
| Context relevance | Diluted | Focused |
| Update complexity | Error-prone | Isolated changes |
| Cross-referencing | Implicit | Explicit in manifest |

---

## Format Tips for AI Consumption

1. **Use structured data where possible** — tables, YAML blocks, JSON schemas are more parseable than prose
2. **Front-load critical info** — put the most important context in first 20% of each file
3. **Explicit over implicit** — state relationships directly, don't assume inference
4. **Consistent headers** — same structure across files helps pattern matching

```markdown
## Component: AuthService
**Purpose:** Handle user authentication
**Depends on:** UserRepository, TokenService
**Exposes:** login(), logout(), refreshToken()
```

---

## Agent-Specific Loading Pattern

```
Architect agent:      reads MANIFEST.md only
API-designer agent:   reads MANIFEST.md → architecture.md
Frontend agent:       reads MANIFEST.md → architecture.md → api-spec.md
Docs-generator:       reads MANIFEST.md → all specs + source code
```

This gives each agent **minimum necessary context** while maintaining coherence through the manifest.

Would you like me to create a template structure for any of these files?