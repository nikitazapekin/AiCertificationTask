# Test Generator (Standalone)

Run test generation via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `test-generator`
- **description:** `Generate tests`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Create comprehensive tests following project patterns.

PROCESS:
1. Determine test type (unit, integration, E2E)
2. Create test structure with factories, fakers, mocks
3. Write tests following project patterns
4. Run tests to verify they pass

TEST TYPE DECISION:
- Single unit (handler, service) → Unit Test
- Database/API interaction → Integration Test
- User workflow → E2E Test

INCLUDE:
- Happy path tests
- Error case tests
- Edge case tests
- Proper mocking

TEST COMMANDS:
npx nx test backend
npx nx test backend -- --testPathPattern=<file>
npx nx test backend -- --coverage

STOP after creating tests. Do not proceed to debugging or other skills.
```

**After sub-agent completes:** Report the test results to the user.
