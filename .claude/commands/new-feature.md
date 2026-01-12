# Complete Feature Implementation Workflow

Implement a complete feature following Clean Architecture and CQRS patterns.

Feature name: $ARGUMENTS

## Phase 1: Planning and Analysis

1. **Requirements Analysis**
   - Review feature requirements
   - Identify entities and relationships
   - Define API endpoints
   - List required error codes

2. **Architecture Planning**
   - Determine if new domain library is needed
   - Identify affected existing modules
   - Plan database schema changes
   - Design command/query flow

## Phase 2: Domain Layer

1. **Create Domain Library** (if needed)
   ```bash
   npx nx g @nx/node:lib <feature-name> --directory=libs/domains/<feature-name>
   ```

2. **Create Folder Structure**
   ```
   src/
   ├── domain/
   │   ├── entities/           # TypeORM entities
   │   ├── interfaces/         # Repository interfaces, UnitOfWork
   │   └── errors/             # Domain-specific errors
   ├── application/
   │   ├── commands/           # Write operations
   │   │   └── <command-name>/
   │   │       ├── <command>.command.ts
   │   │       └── <command>.handler.ts
   │   └── queries/            # Read operations
   │       └── <query-name>/
   │           ├── <query>.query.ts
   │           └── <query>.handler.ts
   ├── infrastructure/
   │   └── repositories/       # TypeORM implementations
   ├── presentation/
   │   ├── controllers/        # NestJS controllers
   │   └── dto/                # Request/response DTOs
   └── index.ts                # Public API exports
   ```

3. **Define Entities**
   - Extend `TypeormEntityBase`
   - Add TypeORM decorators
   - Define relationships

4. **Add Error Codes**
   - Update global `ErrorCode` enum in `@libs/kernel`
   - Create domain-specific error classes

5. **Define Repository Interfaces**
   - Extend `RepositoryPort<Entity, Props>`
   - Define domain-specific methods
   - Create UnitOfWork interface

## Phase 3: Application Layer (CQRS)

1. **Create Commands**
   - One command per write operation
   - Extend `Command` base class
   - Use `CommandProps<T>` for constructor
   - Make properties readonly

2. **Create Command Handlers**
   - Extend `CommandHandlerBase<Command, Result>`
   - Use `@CommandHandler(CommandClass)` decorator
   - Inject domain-specific UnitOfWork
   - Override unitOfWork property with correct type
   - Implement business logic in `handle()`

3. **Create Queries**
   - One query per read operation
   - Extend `Query` base class
   - Keep simple and serializable

4. **Create Query Handlers**
   - Extend `QueryHandlerBase<Query, Result>`
   - Use `@QueryHandler(QueryClass)` decorator
   - Inject domain-specific UnitOfWork
   - Implement data retrieval in `handle()`

5. **Create Handler Arrays**
   ```typescript
   // application/commands/<domain>-commands.handlers.ts
   export const DomainCommandHandlers = [
     CreateHandler,
     UpdateHandler,
     DeleteHandler,
   ];

   // application/queries/<domain>-queries.handlers.ts
   export const DomainQueryHandlers = [
     GetHandler,
     ListHandler,
   ];
   ```

## Phase 4: Infrastructure Layer

1. **Implement Repositories**
   - Extend `TypeormRepositoryBase<Entity, Props>`
   - Implement domain interface methods
   - Use TypeORM QueryBuilder for complex queries

2. **Implement UnitOfWork**
   - Extend `TypeormUnitOfWork`
   - Implement domain-specific UnitOfWork interface
   - Provide repository getters

## Phase 5: Presentation Layer

1. **Create DTOs**
   - Request DTOs with validation decorators
   - Response DTOs with transformation
   - Use `class-transformer` and `class-validator`

2. **Create Controller**
   - Inject `CommandBus` and `QueryBus`
   - Add Swagger decorators (`@ApiTags`, `@ApiOperation`)
   - Map DTOs to Commands/Queries
   - Handle responses

## Phase 6: Module Integration

1. **Create Domain Module**
   ```typescript
   @Module({
     imports: [
       CqrsModule,
       TypeOrmModule.forFeature([Entity]),
     ],
     providers: [
       {
         provide: UnitOfWorkKey,
         useFactory: (dataSource, logger, context) => {
           return new DomainUnitOfWork(logger, context, dataSource);
         },
         inject: [DataSource, LoggerServiceKey, ContextStorageKey],
       },
       ...DomainCommandHandlers,
       ...DomainQueryHandlers,
     ],
     controllers: [DomainController],
     exports: [UnitOfWorkKey],
   })
   export class DomainModule {}
   ```

2. **Add to AppModule**
   ```typescript
   @Module({
     imports: [
       // ... existing imports
       DomainModule,
     ],
   })
   export class AppModule {}
   ```

3. **Update Path Aliases**
   ```json
   // tsconfig.base.json
   {
     "paths": {
       "@domains/<feature-name>": ["libs/domains/<feature-name>/src/index.ts"]
     }
   }
   ```

## Phase 7: Testing

1. **Create Test Structure**
   ```
   __tests__/
   ├── factories/
   │   └── entity.factory.ts
   ├── fakers/
   │   └── entity.faker.ts
   └── mocks/
       ├── repository.mock.ts
       └── unit-of-work.mock.ts
   ```

2. **Write Unit Tests**
   - Command handler tests (business logic)
   - Query handler tests (data retrieval)
   - Repository tests (in-memory SQLite)
   - Entity tests (validations, methods)

3. **Write Integration Tests**
   - Controller tests with TestingModule
   - E2E tests in backend-e2e

4. **Run Tests**
   ```bash
   npx nx test <feature-name>
   npx nx test <feature-name> --coverage
   ```

## Phase 8: Documentation

1. **Update CLAUDE.md**
   - Add new domain to architecture section
   - Document key endpoints
   - Note any special patterns

2. **Create Domain README**
   - Overview and purpose
   - Key entities and relationships
   - API endpoints
   - Usage examples

3. **Swagger Documentation**
   - Verify all endpoints have descriptions
   - Add request/response examples
   - Document error responses

## Phase 9: Quality Assurance

1. **Run Quality Checks**
   ```bash
   npx nx lint <feature-name> --fix
   npx nx test <feature-name>
   npx nx build backend
   ```

2. **Manual Testing**
   - Start dev server: `npx nx serve backend`
   - Test via Swagger UI: http://localhost:3000/docs
   - Verify all CRUD operations
   - Test error scenarios

3. **Code Review Checklist**
   - [ ] CQRS pattern followed correctly
   - [ ] All error codes in global enum
   - [ ] Path aliases used (no relative imports)
   - [ ] Tests have >80% coverage
   - [ ] Swagger docs complete
   - [ ] No console.log statements
   - [ ] TypeScript strict mode passes

## Phase 10: Deployment Preparation

1. **Create Migration** (if schema changes)
   ```bash
   npm run migration:generate -- -n Add<Feature>
   ```

2. **Update Changelog**
   - Document new feature
   - List API changes
   - Note breaking changes

3. **Create Pull Request**
   - Descriptive title and description
   - Link to requirements/issues
   - Add screenshots if UI changes
   - Request appropriate reviewers

Execute each phase systematically and confirm completion before proceeding to the next phase.
