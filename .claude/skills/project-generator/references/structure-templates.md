# Structure Templates

## HTTP API Project

```
src/
├── main.ts
├── app.module.ts
│
├── shared/
│   ├── config/
│   │   ├── config.module.ts
│   │   ├── config.service.ts
│   │   └── env.validation.ts
│   ├── logger/
│   │   ├── logger.module.ts
│   │   └── logger.service.ts
│   ├── errors/
│   │   ├── http-exception.filter.ts
│   │   └── error-codes.ts
│   ├── database/
│   │   └── database.module.ts
│   └── health/
│       ├── health.module.ts
│       └── health.controller.ts
│
├── modules/
│   └── <module-name>/
│       ├── <name>.module.ts
│       ├── <name>.controller.ts
│       ├── <name>.service.ts
│       ├── <name>.repository.ts
│       ├── dto/
│       │   ├── create-<name>.dto.ts
│       │   └── update-<name>.dto.ts
│       └── entities/
│           └── <name>.entity.ts
│
└── bootstrap/
    └── http.bootstrap.ts
```

## Background Worker Project

```
src/
├── main.ts
├── app.module.ts
│
├── shared/
│   ├── config/
│   │   ├── config.module.ts
│   │   ├── config.service.ts
│   │   └── env.validation.ts
│   ├── logger/
│   │   ├── logger.module.ts
│   │   └── logger.service.ts
│   ├── errors/
│   │   └── error-codes.ts
│   └── database/
│       └── database.module.ts
│
├── modules/
│   └── <module-name>/
│       ├── <name>.module.ts
│       ├── <name>.processor.ts
│       ├── <name>.service.ts
│       ├── <name>.repository.ts
│       └── entities/
│           └── <name>.entity.ts
│
└── bootstrap/
    └── worker.bootstrap.ts
```

## Mixed (HTTP + Worker) Project

```
src/
├── main.ts
├── app.module.ts
│
├── shared/
│   ├── config/
│   │   ├── config.module.ts
│   │   ├── config.service.ts
│   │   └── env.validation.ts
│   ├── logger/
│   │   ├── logger.module.ts
│   │   └── logger.service.ts
│   ├── errors/
│   │   ├── http-exception.filter.ts
│   │   └── error-codes.ts
│   ├── database/
│   │   └── database.module.ts
│   └── health/
│       ├── health.module.ts
│       └── health.controller.ts
│
├── modules/
│   └── <module-name>/
│       ├── <name>.module.ts
│       ├── <name>.controller.ts
│       ├── <name>.processor.ts
│       ├── <name>.service.ts
│       ├── <name>.repository.ts
│       ├── dto/
│       │   ├── create-<name>.dto.ts
│       │   └── update-<name>.dto.ts
│       └── entities/
│           └── <name>.entity.ts
│
└── bootstrap/
    ├── http.bootstrap.ts
    └── worker.bootstrap.ts
```

## Module Templates

### Controller (HTTP)

```typescript
import { Controller, Get, Post, Put, Delete, Param, Body } from '@nestjs/common';
import { <Name>Service } from './<name>.service';
import { Create<Name>Dto } from './dto/create-<name>.dto';
import { Update<Name>Dto } from './dto/update-<name>.dto';

@Controller('<name>s')
export class <Name>Controller {
  constructor(private readonly <name>Service: <Name>Service) {}

  @Post()
  create(@Body() dto: Create<Name>Dto) {
    return this.<name>Service.create(dto);
  }

  @Get()
  findAll() {
    return this.<name>Service.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.<name>Service.findOne(id);
  }

  @Put(':id')
  update(@Param('id') id: string, @Body() dto: Update<Name>Dto) {
    return this.<name>Service.update(id, dto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.<name>Service.remove(id);
  }
}
```

### Service

```typescript
import { Injectable } from '@nestjs/common';
import { <Name>Repository } from './<name>.repository';
import { Create<Name>Dto } from './dto/create-<name>.dto';
import { Update<Name>Dto } from './dto/update-<name>.dto';

@Injectable()
export class <Name>Service {
  constructor(private readonly <name>Repository: <Name>Repository) {}

  create(dto: Create<Name>Dto) {
    // TODO: Implement
    throw new Error('Not implemented');
  }

  findAll() {
    // TODO: Implement
    throw new Error('Not implemented');
  }

  findOne(id: string) {
    // TODO: Implement
    throw new Error('Not implemented');
  }

  update(id: string, dto: Update<Name>Dto) {
    // TODO: Implement
    throw new Error('Not implemented');
  }

  remove(id: string) {
    // TODO: Implement
    throw new Error('Not implemented');
  }
}
```

### Repository (TypeORM)

```typescript
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { <Name> } from './entities/<name>.entity';

@Injectable()
export class <Name>Repository {
  constructor(
    @InjectRepository(<Name>)
    private readonly repository: Repository<<Name>>,
  ) {}

  async create(data: Partial<<Name>>): Promise<<Name>> {
    const entity = this.repository.create(data);
    return this.repository.save(entity);
  }

  async findAll(): Promise<<Name>[]> {
    return this.repository.find();
  }

  async findById(id: string): Promise<<Name> | null> {
    return this.repository.findOne({ where: { id } });
  }

  async update(id: string, data: Partial<<Name>>): Promise<<Name> | null> {
    await this.repository.update(id, data);
    return this.findById(id);
  }

  async delete(id: string): Promise<void> {
    await this.repository.delete(id);
  }
}
```

### Repository (Prisma)

```typescript
import { Injectable } from '@nestjs/common';
import { PrismaService } from '../../shared/database/prisma.service';

@Injectable()
export class <Name>Repository {
  constructor(private readonly prisma: PrismaService) {}

  async create(data: any) {
    return this.prisma.<name>.create({ data });
  }

  async findAll() {
    return this.prisma.<name>.findMany();
  }

  async findById(id: string) {
    return this.prisma.<name>.findUnique({ where: { id } });
  }

  async update(id: string, data: any) {
    return this.prisma.<name>.update({ where: { id }, data });
  }

  async delete(id: string) {
    return this.prisma.<name>.delete({ where: { id } });
  }
}
```

### Entity (TypeORM)

```typescript
import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, UpdateDateColumn } from 'typeorm';

@Entity('<name>s')
export class <Name> {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  // TODO: Add entity fields

  @CreateDateColumn()
  createdAt: Date;

  @UpdateDateColumn()
  updatedAt: Date;
}
```

### Module

```typescript
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { <Name>Controller } from './<name>.controller';
import { <Name>Service } from './<name>.service';
import { <Name>Repository } from './<name>.repository';
import { <Name> } from './entities/<name>.entity';

@Module({
  imports: [TypeOrmModule.forFeature([<Name>])],
  controllers: [<Name>Controller],
  providers: [<Name>Service, <Name>Repository],
  exports: [<Name>Service],
})
export class <Name>Module {}
```

### DTO Templates

```typescript
// create-<name>.dto.ts
export class Create<Name>Dto {
  // TODO: Add fields with class-validator decorators
}

// update-<name>.dto.ts
import { PartialType } from '@nestjs/mapped-types';
import { Create<Name>Dto } from './create-<name>.dto';

export class Update<Name>Dto extends PartialType(Create<Name>Dto) {}
```

### Processor (Background Worker)

```typescript
import { Processor, Process } from '@nestjs/bull';
import { Job } from 'bull';
import { <Name>Service } from './<name>.service';

@Processor('<name>-queue')
export class <Name>Processor {
  constructor(private readonly <name>Service: <Name>Service) {}

  @Process()
  async handle(job: Job) {
    // TODO: Implement job processing
    throw new Error('Not implemented');
  }
}
```

## ARCHITECTURE.md Template

```markdown
# Architecture Documentation

## Overview

[Service description from user input]

## Project Structure

\`\`\`
src/
├── main.ts              # Application entry point
├── app.module.ts        # Root module
├── shared/              # Cross-cutting infrastructure
├── modules/             # Feature modules
└── bootstrap/           # Bootstrap configurations
\`\`\`

## Modules

| Module | Responsibility |
|--------|----------------|
| [module] | [description] |

## Architecture Style

**Layered Architecture:**
- **Controller**: HTTP request handling, input validation
- **Service**: Business logic, orchestration
- **Repository**: Data access, persistence

## Dependencies

\`\`\`
Controller → Service → Repository → Database
\`\`\`

## Development Commands

\`\`\`bash
# Start development server
npm run start:dev

# Build for production
npm run build

# Run tests
npm run test

# Run linter
npm run lint
\`\`\`

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| PORT | HTTP port | 3000 |
| NODE_ENV | Environment | development |
| DATABASE_URL | Database connection string | - |
\`\`\`
```
