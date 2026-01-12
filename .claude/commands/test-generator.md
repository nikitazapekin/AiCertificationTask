# Test Generator (Standalone)

Run the test-generator skill to create comprehensive tests.

**Important:** This command runs the skill in isolation WITHOUT automatically triggering next steps.

## Input
$ARGUMENTS

## Instructions

Use the `test-generator` skill to:
1. Determine test type (unit, integration, E2E)
2. Create test structure with factories, fakers, mocks
3. Write tests following project patterns
4. Run tests to verify they pass

Test type decision:
- Single unit (handler, service) → Unit Test
- Database/API interaction → Integration Test
- User workflow → E2E Test

Include:
- Happy path tests
- Error case tests
- Edge case tests
- Proper mocking

Commands:
```bash
npx nx test backend
npx nx test backend -- --testPathPattern=<file>
npx nx test backend -- --coverage
```

**STOP after creating tests.** Do not automatically proceed to debugging or other skills.
