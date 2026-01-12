---
name: api-designer
description: Design REST APIs with proper conventions, DTOs, Swagger docs, and Bruno collections. Use when creating endpoints, designing DTOs, adding Swagger decorators, generating API documentation, or creating Bruno/Postman collections. Triggers on "API design", "create endpoint", "DTO", "swagger", "openapi", "bruno collection", "API documentation".
---

# API Designer

## Overview

Design REST APIs following conventions with DTOs, Swagger documentation, and Bruno collections.

## REST Conventions

### URL Naming

```
# Resources (nouns, plural)
GET    /users           # List
POST   /users           # Create
GET    /users/:id       # Get one
PUT    /users/:id       # Full update
PATCH  /users/:id       # Partial update
DELETE /users/:id       # Delete

# Nested resources
GET    /users/:id/posts     # User's posts
POST   /users/:id/posts     # Create post for user

# Actions (verbs for non-CRUD)
POST   /users/:id/activate
POST   /orders/:id/cancel
```

### HTTP Methods & Status Codes

| Method | Success | Purpose |
|--------|---------|---------|
| GET | 200 | Retrieve resource(s) |
| POST | 201 | Create resource |
| PUT | 200 | Full update |
| PATCH | 200 | Partial update |
| DELETE | 204 | Delete resource |

### Error Responses

```typescript
{
  "statusCode": 400,
  "message": "Validation failed",
  "error": "Bad Request",
  "errorCode": "VALIDATION_ERROR",
  "details": [
    { "field": "email", "message": "Invalid email format" }
  ]
}
```

## DTO Patterns

### Request DTOs

```typescript
// create-user.dto.ts
import { IsEmail, IsNotEmpty, MaxLength, IsOptional } from 'class-validator';
import { ApiProperty, ApiPropertyOptional } from '@nestjs/swagger';

export class CreateUserDto {
  @ApiProperty({ example: 'john@example.com', description: 'User email' })
  @IsEmail()
  @MaxLength(255)
  email: string;

  @ApiProperty({ example: 'John', maxLength: 100 })
  @IsNotEmpty()
  @MaxLength(100)
  firstName: string;

  @ApiPropertyOptional({ example: 'Software Engineer' })
  @IsOptional()
  @MaxLength(255)
  title?: string;
}
```

### Update DTOs

```typescript
// update-user.dto.ts
import { PartialType, OmitType } from '@nestjs/swagger';

// All fields optional except email
export class UpdateUserDto extends PartialType(
  OmitType(CreateUserDto, ['email'] as const)
) {}
```

### Response DTOs

```typescript
// user-response.dto.ts
import { ApiProperty } from '@nestjs/swagger';
import { Exclude, Expose } from 'class-transformer';

export class UserResponseDto {
  @ApiProperty()
  @Expose()
  id: number;

  @ApiProperty()
  @Expose()
  email: string;

  @ApiProperty()
  @Expose()
  firstName: string;

  @Exclude()
  password: string; // Never expose

  static fromEntity(entity: User): UserResponseDto {
    const dto = new UserResponseDto();
    dto.id = entity.id;
    dto.email = entity.email;
    dto.firstName = entity.firstName;
    return dto;
  }
}
```

## Swagger Decorators

### Controller Level

```typescript
@ApiTags('users')
@Controller('users')
export class UserController {
  // ...
}
```

### Endpoint Level

```typescript
@Post()
@ApiOperation({ summary: 'Create a new user' })
@ApiBody({ type: CreateUserDto })
@ApiResponse({ status: 201, description: 'User created', type: UserResponseDto })
@ApiResponse({ status: 400, description: 'Validation error' })
@ApiResponse({ status: 409, description: 'Email already exists' })
async createUser(@Body() dto: CreateUserDto): Promise<UserResponseDto> {
  // ...
}

@Get(':id')
@ApiOperation({ summary: 'Get user by ID' })
@ApiParam({ name: 'id', type: Number })
@ApiResponse({ status: 200, type: UserResponseDto })
@ApiResponse({ status: 404, description: 'User not found' })
async getUser(@Param('id', ParseIntPipe) id: number): Promise<UserResponseDto> {
  // ...
}
```

### Query Parameters

```typescript
@Get()
@ApiOperation({ summary: 'List users with pagination' })
@ApiQuery({ name: 'page', required: false, type: Number })
@ApiQuery({ name: 'limit', required: false, type: Number })
@ApiQuery({ name: 'search', required: false, type: String })
async listUsers(
  @Query('page', new DefaultValuePipe(1), ParseIntPipe) page: number,
  @Query('limit', new DefaultValuePipe(10), ParseIntPipe) limit: number,
  @Query('search') search?: string,
): Promise<PaginatedResponseDto<UserResponseDto>> {
  // ...
}
```

## Controller Template

```typescript
import { Controller, Get, Post, Put, Delete, Body, Param, Query, ParseIntPipe } from '@nestjs/common';
import { ApiTags, ApiOperation, ApiResponse, ApiParam, ApiQuery } from '@nestjs/swagger';
import { CommandBus, QueryBus } from '@nestjs/cqrs';

@ApiTags('users')
@Controller('users')
export class UserController {
  constructor(
    private readonly commandBus: CommandBus,
    private readonly queryBus: QueryBus,
  ) {}

  @Post()
  @ApiOperation({ summary: 'Create user' })
  @ApiResponse({ status: 201, type: UserResponseDto })
  async create(@Body() dto: CreateUserDto): Promise<UserResponseDto> {
    const command = new CreateUserCommand(dto);
    const id = await this.commandBus.execute(command);
    const user = await this.queryBus.execute(new GetUserQuery(id));
    return UserResponseDto.fromEntity(user);
  }

  @Get(':id')
  @ApiOperation({ summary: 'Get user by ID' })
  @ApiParam({ name: 'id', type: Number })
  @ApiResponse({ status: 200, type: UserResponseDto })
  async findOne(@Param('id', ParseIntPipe) id: number): Promise<UserResponseDto> {
    const user = await this.queryBus.execute(new GetUserQuery(id));
    return UserResponseDto.fromEntity(user);
  }
}
```

## Integration

**Called by:**
- `architect` - After architecture design
- `new-feature` - Phase 3

**Calls:**
- `coder` - For implementation
- `test-generator` - For API tests
