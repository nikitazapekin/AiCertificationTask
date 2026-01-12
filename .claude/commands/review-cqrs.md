# CQRS Pattern Code Review

Perform a comprehensive code review focused on CQRS pattern implementation.

## Review Focus Areas

### 1. Command/Query Separation
- **Commands**: Verify all write operations extend `CommandHandlerBase`
- **Queries**: Verify all read operations extend `QueryHandlerBase`
- Check that Commands are wrapped in transactions (automatic via CommandHandlerBase)
- Check that Queries are read-only (no transactions)

### 2. Command Structure
```typescript
// Commands should:
- Extend Command base class
- Have immutable properties (readonly)
- Include correlationId (auto-generated)
- Use CommandProps<T> for constructor
```

### 3. Command Handler Structure
```typescript
// Command handlers should:
- Extend CommandHandlerBase
- Inject IUnitOfWork via constructor
- Use @CommandHandler(CommandName) decorator
- Override unitOfWork with domain-specific type
- Implement handle() method with business logic
```

### 4. Query Structure
```typescript
// Queries should:
- Extend Query base class
- Have simple properties (no complex objects)
- Be serializable
```

### 5. Query Handler Structure
```typescript
// Query handlers should:
- Extend QueryHandlerBase
- Inject IUnitOfWork via constructor
- Use @QueryHandler(QueryName) decorator
- Implement handle() method returning data
- NOT use transactions (read-only)
```

### 6. Module Registration
Check that handlers are properly registered:
```typescript
@Module({
  imports: [CqrsModule],
  providers: [
    ...CommandHandlers,  // Array of command handlers
    ...QueryHandlers,    // Array of query handlers
  ]
})
```

### 7. Controller Usage
Verify controllers use CommandBus and QueryBus:
```typescript
constructor(
  private readonly commandBus: CommandBus,
  private readonly queryBus: QueryBus
) {}

// Commands
await this.commandBus.execute(new SomeCommand({ ... }));

// Queries
await this.queryBus.execute(new SomeQuery(...));
```

## Anti-Patterns to Flag

❌ **Commands without transactions**
- All commands must extend CommandHandlerBase (auto-transaction)

❌ **Queries in transactions**
- Queries should be read-only, no unitOfWork.execute()

❌ **Business logic in controllers**
- Controllers should only dispatch commands/queries

❌ **Direct repository calls in controllers**
- Always use command/query handlers

❌ **Missing override keyword**
- When extending unitOfWork property in handlers

❌ **Manual correlation ID management**
- Use Command base class auto-generation

## Files to Review
Review: $ARGUMENTS

Provide specific recommendations with file:line references.
