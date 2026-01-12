# Skill Creator (Standalone)

Run the skill-creator skill to create or update Claude skills.

**Important:** This command runs the skill in isolation.

## Input
$ARGUMENTS

## Instructions

Use the `skill-creator` skill to:
1. Understand the skill with concrete examples
2. Plan reusable contents (scripts, references, assets)
3. Initialize skill structure
4. Edit SKILL.md and resources
5. Package the skill

Skill structure:
```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/     - Executable code
    ├── references/  - Documentation
    └── assets/      - Output files
```

Core principles:
- **Concise is key** - Context window is shared
- **Set appropriate freedom** - Match specificity to task fragility
- **Progressive disclosure** - Load content as needed

SKILL.md guidelines:
- Keep under 500 lines
- Description is the trigger mechanism
- Use imperative/infinitive form
- Reference bundled resources clearly

**Complete skill creation or update as requested.**
