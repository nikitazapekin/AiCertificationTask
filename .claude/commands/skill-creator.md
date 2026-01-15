# Skill Creator (Standalone)

Run skill creation via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `skill-creator`
- **description:** `Create Claude skill`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Create or update Claude skills.

PROCESS:
1. Understand the skill with concrete examples
2. Plan reusable contents (scripts, references, assets)
3. Initialize skill structure
4. Edit SKILL.md and resources
5. Package the skill

SKILL STRUCTURE:
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/     - Executable code
    ├── references/  - Documentation
    └── assets/      - Output files

CORE PRINCIPLES:
- **Concise is key** - Context window is shared
- **Set appropriate freedom** - Match specificity to task fragility
- **Progressive disclosure** - Load content as needed

SKILL.MD GUIDELINES:
- Keep under 500 lines
- Description is the trigger mechanism
- Use imperative/infinitive form
- Reference bundled resources clearly

Complete skill creation or update as requested.
```

**After sub-agent completes:** Report the skill creation status to the user.
