---
name: project-generator
description: Generate project structure for Backend (NestJS) or Frontend (React). Use for new projects, scaffolding, initial setup, or creating module/component structure. Triggers on "generate project", "scaffold", "create structure", "new project", "project setup", "init project", "create frontend", "create backend". Creates minimal infrastructure and empty stubs. Does NOT implement business logic or features.
---

# Project Generator

Generate clean, standardized project structures for Backend (NestJS) or Frontend (React).

## Scope

**GENERATES:**
- Project folder structure
- Module/Component boundaries
- Empty controllers/services/repositories (backend) or components/hooks (frontend)
- Minimal shared infrastructure
- Application bootstrap structure
- ARCHITECTURE.md documentation

**DOES NOT GENERATE:**
- Business logic or use cases
- Feature-specific functionality
- Filled DTOs or component implementations

## Workflow

```
1. ASK PROJECT TYPE → 2. ASK QUESTIONS → 3. INFER DEFAULTS → 4. GENERATE STRUCTURE → 5. CREATE DOCUMENTATION
```

### Step 1: Ask Project Type

First question. **Use AskUserQuestion tool.**

```markdown
## What type of project?

1. **Backend** - NestJS with layered architecture
2. **Frontend** - React with component-based architecture
3. **Full-stack** - Both backend and frontend
```

---

# BACKEND (NestJS)

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

## Backend Questions

Ask only essential questions. **Use AskUserQuestion tool.**

```markdown
## Backend Setup Questions

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

## Backend Defaults

If not specified, assume:
- Service type: HTTP API
- Database: PostgreSQL + TypeORM
- No external integrations

## Backend Structure

```
apps/backend/src/
├── main.ts
├── app.module.ts
├── shared/
│   ├── config/
│   │   ├── config.module.ts
│   │   └── config.service.ts
│   ├── logger/
│   │   ├── logger.module.ts
│   │   └── logger.service.ts
│   ├── database/
│   │   └── database.module.ts
│   ├── errors/
│   │   ├── errors.filter.ts
│   │   └── error-codes.enum.ts
│   └── health/
│       ├── health.module.ts
│       └── health.controller.ts
└── modules/
    └── <name>/
        ├── <name>.module.ts
        ├── <name>.controller.ts
        ├── <name>.service.ts
        ├── <name>.repository.ts
        ├── dto/
        │   ├── create-<name>.dto.ts
        │   └── update-<name>.dto.ts
        └── entities/
            └── <name>.entity.ts
```

## Backend Shared Modules

| Module | Purpose | When to Include |
|--------|---------|-----------------|
| Config | Environment configuration | Always |
| Logger | Structured logging | Always |
| Errors | Global error handling | Always |
| Database | TypeORM/Prisma/Mongoose connection | If database selected |
| Health | Health check endpoints | Always for HTTP APIs |

---

# FRONTEND (React)

## Architecture Rules

**COMPONENT-BASED ARCHITECTURE:**
```
Pages → Features → Components → Hooks
```

**TECH STACK:**
- React 18+ with TypeScript
- React Router for routing
- React Query (TanStack Query) for server state
- Zustand for client state (if needed)
- CSS Modules or Tailwind for styling

**FORBIDDEN PATTERNS:**
- Class components
- Redux (use Zustand if global state needed)
- CSS-in-JS libraries (styled-components, emotion)

## Frontend Questions

Ask only essential questions. **Use AskUserQuestion tool.**

```markdown
## Frontend Setup Questions

1. **App purpose** (1-3 sentences): What does this app do?

2. **Main pages/routes** (e.g., Home, Dashboard, Settings):
   List the main pages needed.

3. **Features/domains** (e.g., Auth, Users, Products):
   List the main feature areas.

4. **Styling approach:**
   - [ ] CSS Modules
   - [ ] Tailwind CSS
   - [ ] Plain CSS

5. **State management:**
   - [ ] React Query only (recommended for most apps)
   - [ ] React Query + Zustand (for complex client state)
   - [ ] React Query + Context (for simple shared state)

6. **API integration:**
   - [ ] REST API (specify base URL if known)
   - [ ] No API yet (mock data)
```

## Frontend Defaults

If not specified, assume:
- Styling: Tailwind CSS
- State: React Query only
- API: REST API with mock data fallback

## Frontend Structure

```
apps/frontend/src/
├── main.tsx
├── App.tsx
├── index.css
├── vite-env.d.ts
├── api/
│   ├── client.ts              # Axios/fetch wrapper
│   └── endpoints/
│       └── <feature>.api.ts   # API functions per feature
├── components/
│   ├── ui/                    # Reusable UI components
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.module.css
│   │   │   └── index.ts
│   │   ├── Input/
│   │   ├── Modal/
│   │   └── Card/
│   └── layout/                # Layout components
│       ├── Header/
│       ├── Sidebar/
│       ├── Footer/
│       └── PageLayout/
├── features/
│   └── <feature>/
│       ├── components/        # Feature-specific components
│       │   └── <Component>.tsx
│       ├── hooks/             # Feature-specific hooks
│       │   └── use-<feature>.ts
│       ├── types/             # Feature types
│       │   └── <feature>.types.ts
│       └── index.ts           # Public exports
├── hooks/                     # Shared hooks
│   ├── use-auth.ts
│   └── use-api.ts
├── pages/
│   ├── HomePage/
│   │   ├── HomePage.tsx
│   │   └── index.ts
│   ├── DashboardPage/
│   └── NotFoundPage/
├── providers/
│   ├── QueryProvider.tsx      # React Query setup
│   ├── AuthProvider.tsx       # Auth context
│   └── ThemeProvider.tsx      # Theme context (optional)
├── routes/
│   ├── routes.tsx             # Route definitions
│   └── ProtectedRoute.tsx     # Auth guard
├── styles/
│   ├── variables.css          # CSS variables
│   └── globals.css            # Global styles
├── types/
│   └── common.types.ts        # Shared types
└── utils/
    ├── format.ts              # Formatting utilities
    └── validation.ts          # Validation utilities
```

## Frontend Component Template

```typescript
// components/ui/Button/Button.tsx
import React from 'react';
import styles from './Button.module.css';

interface ButtonProps {
  children: React.ReactNode;
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  onClick?: () => void;
  type?: 'button' | 'submit' | 'reset';
  className?: string;
}

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = 'primary',
  size = 'md',
  disabled = false,
  onClick,
  type = 'button',
  className,
}) => {
  return (
    <button
      type={type}
      className={`${styles.button} ${styles[variant]} ${styles[size]} ${className || ''}`}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
};

Button.displayName = 'Button';
```

## Frontend Hook Template

```typescript
// features/users/hooks/use-users.ts
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { usersApi } from '@/api/endpoints/users.api';
import type { User, CreateUserDto } from '../types/users.types';

export function useUsers() {
  return useQuery({
    queryKey: ['users'],
    queryFn: usersApi.getAll,
  });
}

export function useUser(id: string) {
  return useQuery({
    queryKey: ['users', id],
    queryFn: () => usersApi.getById(id),
    enabled: !!id,
  });
}

export function useCreateUser() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (data: CreateUserDto) => usersApi.create(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['users'] });
    },
  });
}
```

## Frontend API Template

```typescript
// api/client.ts
import axios from 'axios';

export const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL || '/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// api/endpoints/users.api.ts
import { apiClient } from '../client';
import type { User, CreateUserDto, UpdateUserDto } from '@/features/users/types/users.types';

export const usersApi = {
  getAll: async (): Promise<User[]> => {
    const { data } = await apiClient.get('/users');
    return data;
  },

  getById: async (id: string): Promise<User> => {
    const { data } = await apiClient.get(`/users/${id}`);
    return data;
  },

  create: async (dto: CreateUserDto): Promise<User> => {
    const { data } = await apiClient.post('/users', dto);
    return data;
  },

  update: async (id: string, dto: UpdateUserDto): Promise<User> => {
    const { data } = await apiClient.patch(`/users/${id}`, dto);
    return data;
  },

  delete: async (id: string): Promise<void> => {
    await apiClient.delete(`/users/${id}`);
  },
};
```

## Frontend Page Template

```typescript
// pages/HomePage/HomePage.tsx
import React from 'react';
import { PageLayout } from '@/components/layout/PageLayout';

export const HomePage: React.FC = () => {
  return (
    <PageLayout title="Home">
      <div>
        <h1>Welcome</h1>
        {/* Page content */}
      </div>
    </PageLayout>
  );
};

HomePage.displayName = 'HomePage';
```

## Frontend File Naming

| Type | Pattern | Example |
|------|---------|---------|
| Component | `PascalCase/PascalCase.tsx` | `Button/Button.tsx` |
| Hook | `use-kebab-case.ts` | `use-users.ts` |
| API | `<feature>.api.ts` | `users.api.ts` |
| Types | `<feature>.types.ts` | `users.types.ts` |
| Styles | `*.module.css` | `Button.module.css` |
| Page | `PascalCasePage/PascalCasePage.tsx` | `HomePage/HomePage.tsx` |

---

# FULL-STACK

For full-stack projects, generate both structures in a monorepo:

```
project-root/
├── apps/
│   ├── backend/     # NestJS structure
│   └── frontend/    # React structure
├── libs/            # Shared libraries (types, utils)
│   └── shared/
│       └── types/
├── package.json     # Root package.json with workspaces
├── nx.json          # Nx configuration (optional)
└── ARCHITECTURE.md
```

---

## Output Checklist

### Backend
- [ ] All folders created
- [ ] All modules have `.module.ts`
- [ ] Controllers have basic CRUD routes (empty)
- [ ] Services have method stubs
- [ ] Repositories have TypeORM/Prisma setup
- [ ] `app.module.ts` imports all modules

### Frontend
- [ ] All folders created
- [ ] Pages have route definitions
- [ ] Features have component/hook/types structure
- [ ] API client configured
- [ ] Providers set up (Query, Auth)
- [ ] UI components have proper structure

### Both
- [ ] `ARCHITECTURE.md` is complete

---

## Next Steps

After project structure is generated, STOP and present these options:

**Next by flow:** `/git-worktrees [context]` - Create isolated workspace for development.

**Alternatives:**
- `/coder [context]` - Start backend implementation directly (skip worktrees for simple projects).
- `/frontend-design [context]` - Design UI before frontend implementation.
