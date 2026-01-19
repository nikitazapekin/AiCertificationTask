---
name: writing-plans
description: Use when you have a spec or requirements for a multi-step task, before touching code. Creates detailed implementation plans with bite-sized tasks for engineers with zero codebase context.
---

# Writing Plans

## Overview

Write comprehensive implementation plans assuming the engineer has zero context for our codebase and questionable taste. Document everything they need to know: which files to touch for each task, code, testing, docs they might need to check, how to test it. Give them the whole plan as bite-sized tasks. DRY. YAGNI. TDD. Frequent commits.

**Announce at start:** "I'm using the writing-plans skill to create the implementation plan."

**Save plans to:** `docs/plans/YYYY-MM-DD-<feature-name>.md`

## Bite-Sized Task Granularity

**Each step is one action (2-5 minutes):**
- "Write the failing test" - step
- "Run it to make sure it fails" - step
- "Implement the minimal code to make the test pass" - step
- "Run the tests and make sure they pass" - step
- "Commit" - step

## Plan Document Header

**Every plan MUST start with this header:**

```markdown
# [Feature Name] Implementation Plan

> **For Claude:** Use `using-git-worktrees` to create isolated workspace, then implement with `coder` skill.

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about approach]

**Tech Stack:** [Key technologies/libraries]

---
```

## Task Structure

```markdown
### Task N: [Component Name]

**Files:**
- Create: `exact/path/to/file.ts`
- Modify: `exact/path/to/existing.ts:123-145`
- Test: `exact/path/__tests__/file.spec.ts`

**Step 1: Write the failing test**

\`\`\`typescript
describe('ComponentName', () => {
  it('should do specific thing', () => {
    const result = doThing(input);
    expect(result).toBe(expected);
  });
});
\`\`\`

**Step 2: Run test to verify it fails**

Run: `npx nx test project -- --testPathPattern=file.spec.ts`
Expected: FAIL with "function not defined"

**Step 3: Write minimal implementation**

\`\`\`typescript
export function doThing(input: InputType): OutputType {
  return expected;
}
\`\`\`

**Step 4: Run test to verify it passes**

Run: `npx nx test project -- --testPathPattern=file.spec.ts`
Expected: PASS

**Step 5: Commit**

\`\`\`bash
git add path/to/files
git commit -m "feat(domain): add specific feature"
\`\`\`
```

## Remember

- Exact file paths always
- Complete code in plan (not "add validation")
- Exact commands with expected output
- Reference relevant skills with backticks
- DRY, YAGNI, TDD, frequent commits

## Execution Handoff

After saving the plan, offer execution choice:

**"Plan complete and saved to `docs/plans/<filename>.md`. Execution options:**

**1. Execute Now** - Use `/coder` to implement in current workspace

**2. Isolated Workspace** - Use `/git-worktrees` to create isolated workspace, then `/coder`

**Which approach?"**

---

## Next Steps

After the plan is complete and saved, STOP and present these options:

**Next by flow:** `/architect [context]` - Review architecture decisions before implementation.

**Alternatives:**
- `/git-worktrees [context]` - Create isolated workspace for development.
- `/coder [context]` - Start implementing directly in current workspace.
