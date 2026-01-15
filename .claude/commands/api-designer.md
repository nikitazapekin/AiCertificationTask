# API Designer (Standalone)

Run API design via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `api-designer`
- **description:** `Design REST API`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Design REST APIs with DTOs and Swagger documentation.

PROCESS:
1. Design REST endpoints following conventions (nouns, plural, proper HTTP methods)
2. Create request DTOs with validation decorators
3. Create response DTOs with transformation
4. Add Swagger decorators for documentation
5. Define error response formats

OUTPUT:
- URL naming patterns
- HTTP methods and status codes
- DTO code with validation
- Swagger decorator examples
- Controller template

STOP after completing API design. Do not proceed to implementation or testing.
```

**After sub-agent completes:** Report the API design to the user.
