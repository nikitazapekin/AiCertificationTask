# Documentation Generator (Standalone)

Run the documentation-generator skill to create and maintain documentation.

**Important:** This command runs the skill in isolation WITHOUT automatically triggering next steps (reflect, etc.).

## Input
$ARGUMENTS

## Instructions

Use the `documentation-generator` skill to create:
1. Library README (overview, usage, API reference)
2. Domain README (architecture, endpoints, services)
3. ADR (Architecture Decision Record)
4. Changelog entry
5. JSDoc comments

Documentation locations:
- `libs/<name>/README.md` - Library docs
- `docs/adrs/` - Architecture decisions
- `CHANGELOG.md` - Version history
- `CLAUDE.md` - AI context patterns

Checklist for new feature:
- [ ] README updated
- [ ] ADR if architectural decision
- [ ] Changelog entry
- [ ] JSDoc for public functions

**STOP after completing documentation.** Do not automatically proceed to reflection or other skills.
