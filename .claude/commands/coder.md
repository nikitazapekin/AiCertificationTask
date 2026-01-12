# Coder Backend (Standalone)

Run the coder skill to implement backend features following layered architecture.

**Important:** This command runs the skill in isolation WITHOUT automatically triggering next steps (code-reviewer, test-generator, etc.).

## Input
$ARGUMENTS

## Instructions

Use the `coder` skill to:
1. Understand existing codebase patterns
2. Plan implementation (files to create/modify)
3. Implement following layered architecture
4. Write unit tests
5. Run lint and tests

Layer placement:
- Controller → Presentation layer
- Service → Business Logic layer
- Repository → Data Access layer
- DTO → Data Transfer
- Entity → Domain

Dependency rules:
- ✅ Controller → Service → Repository
- ❌ Repository → Service, Service → Controller

**STOP after completing implementation.** Do not automatically proceed to code review or other skills.
