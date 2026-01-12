# Verification Before Completion (Standalone)

Run the verification-before-completion skill to verify work before claiming completion.

**Important:** This command runs the skill in isolation.

## Input
$ARGUMENTS

## Instructions

Use the `verification-before-completion` skill with the iron law:
**NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE**

The gate function:
1. IDENTIFY: What command proves this claim?
2. RUN: Execute the FULL command (fresh, complete)
3. READ: Full output, check exit code, count failures
4. VERIFY: Does output confirm the claim?
5. ONLY THEN: Make the claim

Verification commands:
```bash
# Tests
npx nx test backend

# Lint
npx nx lint backend

# Build
npx nx build backend

# All
npx nx run-many -t test,lint,build
```

Red flags:
- Using "should", "probably", "seems to"
- Expressing satisfaction before verification
- About to commit/push without verification
- Relying on partial verification

**Run the command. Read the output. THEN claim the result.**
