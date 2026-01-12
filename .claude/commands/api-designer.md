# API Designer (Standalone)

Run the api-designer skill to design REST APIs with DTOs and Swagger docs.

**Important:** This command runs the skill in isolation WITHOUT automatically triggering next steps (coder, test-generator, etc.).

## Input
$ARGUMENTS

## Instructions

Use the `api-designer` skill to:
1. Design REST endpoints following conventions (nouns, plural, proper HTTP methods)
2. Create request DTOs with validation decorators
3. Create response DTOs with transformation
4. Add Swagger decorators for documentation
5. Define error response formats

Provide:
- URL naming patterns
- HTTP methods and status codes
- DTO code with validation
- Swagger decorator examples
- Controller template

**STOP after completing API design.** Do not automatically proceed to implementation or testing.
