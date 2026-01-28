---
name: coder
description: Implement features, fix bugs, and refactor code following layered architecture (Controller/Service/Repository). Use for feature implementation, bug fixes, refactoring, and business logic development. Triggers on "implement", "add feature", "fix", "refactor", "code", "build".
---

# Coder (Backend)

## Overview

Implement backend features, fix bugs, and refactor code following project architecture and conventions.

**Related skills:**
- `architect` - Architecture decisions
- `api-designer` - API design and DTOs

## Project Structure Requirement

**CRITICAL:** All backend code MUST be created inside the `backend/` directory in the project root.

```
project-root/
├── backend/           ← ALL backend code goes here
│   ├── src/
│   │   ├── controllers/
│   │   ├── services/
│   │   ├── repositories/
│   │   ├── entities/
│   │   ├── dto/
│   │   └── modules/
│   ├── test/
│   ├── package.json
│   └── tsconfig.json
└── frontend/          ← Frontend code (separate)
```

**Why:** This prevents merge conflicts when backend and frontend branches are merged. Never create `src/`, `package.json`, or other backend files directly in the project root.

**Before starting:** Verify `backend/` directory exists. If not, create it first.

## Implementation Workflow

```
1. UNDERSTAND → 2. PLAN → 3. IMPLEMENT → 4. TEST → 5. REVIEW
```

### Step 1: Understand

- Review existing codebase patterns
- Identify relevant files and structure
- Understand the current implementation

### Step 2: Plan

- Identify files to create/modify
- Determine architecture layer placement
- Plan tests needed
- Consider edge cases

### Step 3: Implement

Follow established patterns:
- Use consistent file structure
- Add proper TypeScript types
- Handle errors appropriately
- Follow layered architecture

### Step 4: Test

- Write unit tests
- Run tests
- Fix any failures

### Step 5: Review

- Check code quality
- Verify architecture compliance
- Run linter

## Architecture Compliance

### Layer Placement (Layered Architecture)

| Component | Layer | Location |
|-----------|-------|----------|
| Controller | Presentation | `controllers/` or `<module>.controller.ts` |
| Service | Business Logic | `services/` or `<module>.service.ts` |
| Repository | Data Access | `repositories/` or `<module>.repository.ts` |
| DTO | Data Transfer | `dto/` |
| Entity | Domain | `entities/` |

### Dependency Rules

```
✅ ALLOWED:
Controller → Service → Repository
Any layer → shared utilities

❌ NOT ALLOWED:
Repository → Service
Service → Controller
```

## Code Patterns

### Entity

```typescript
import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

@Entity('products')
export class Product {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ unique: true, length: 50 })
  sku: string;

  @Column({ length: 255 })
  name: string;

  @Column({ type: 'decimal', precision: 10, scale: 2 })
  price: number;
}
```

### Repository

```typescript
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Product } from '../entities/product.entity';

@Injectable()
export class ProductRepository {
  constructor(
    @InjectRepository(Product)
    private readonly repository: Repository<Product>,
  ) {}

  async findBySku(sku: string): Promise<Product | null> {
    return this.repository.findOne({ where: { sku } });
  }

  async create(data: Partial<Product>): Promise<Product> {
    const entity = this.repository.create(data);
    return this.repository.save(entity);
  }
}
```

### Service

```typescript
import { Injectable, NotFoundException } from '@nestjs/common';
import { ProductRepository } from '../repositories/product.repository';

@Injectable()
export class ProductService {
  constructor(private readonly productRepository: ProductRepository) {}

  async findById(id: number): Promise<Product> {
    const product = await this.productRepository.findById(id);
    if (!product) {
      throw new NotFoundException(`Product ${id} not found`);
    }
    return product;
  }
}
```

### Controller

```typescript
import { Controller, Get, Post, Body, Param } from '@nestjs/common';
import { ProductService } from '../services/product.service';
import { CreateProductDto } from '../dto/create-product.dto';

@Controller('products')
export class ProductController {
  constructor(private readonly productService: ProductService) {}

  @Get(':id')
  async findById(@Param('id') id: number) {
    return this.productService.findById(id);
  }

  @Post()
  async create(@Body() dto: CreateProductDto) {
    return this.productService.create(dto);
  }
}
```

## File Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Entity | `<name>.entity.ts` | `user.entity.ts` |
| Repository | `<name>.repository.ts` | `user.repository.ts` |
| Service | `<name>.service.ts` | `user.service.ts` |
| Controller | `<name>.controller.ts` | `user.controller.ts` |
| DTO | `<action>-<name>.dto.ts` | `create-user.dto.ts` |
| Module | `<name>.module.ts` | `user.module.ts` |
| Test | `<name>.spec.ts` | `user.service.spec.ts` |

## Quality Checklist

Before completing any implementation:

- [ ] Code follows project conventions
- [ ] Proper error handling
- [ ] Types are explicit (no `any`)
- [ ] Unit tests added
- [ ] Lint passes
- [ ] Tests pass
- [ ] Build succeeds

---

## Next Steps

After implementation is complete, STOP and present these options:

**Next by flow:** `/code-reviewer [context]` - Review the implemented code for quality and issues.

**Alternatives:**
- `/test-generator [context]` - Generate tests for the implementation.
- `/debugger [context]` - Debug if there are issues with the implementation.
