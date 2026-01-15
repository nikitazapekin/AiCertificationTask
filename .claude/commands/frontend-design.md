# Frontend Design (Standalone)

Run frontend design via isolated sub-agent for context management.

**Important:** This command executes in a sub-agent to isolate context and keep main conversation under 100k tokens.

## Input
$ARGUMENTS

## Instructions

**EXECUTE VIA SUB-AGENT:**

Use the Task tool with these parameters:
- **subagent_type:** `frontend-design`
- **description:** `Design frontend UI`
- **prompt:** Include the user input below and the task instructions

### Prompt to Send to Sub-Agent

```
USER INPUT: [Insert $ARGUMENTS here]

TASK: Create distinctive, production-grade UI design specification.

PROCESS:
1. Understand context (purpose, audience, brand, constraints)
2. Choose bold aesthetic direction (not generic)
3. Define typography, color palette, motion strategy
4. Create the memorable element that makes it unforgettable
5. Design component visual specs

AESTHETIC OPTIONS:
- Brutally Minimal, Maximalist Chaos, Retro-Futuristic
- Organic/Natural, Luxury/Refined, Playful/Toy-like
- Editorial/Magazine, Brutalist/Raw, Art Deco/Geometric

AVOID AI SLOP:
- No generic fonts (Inter, Roboto, Arial)
- No purple-to-blue gradients on white
- No cookie-cutter card layouts

STOP after completing design specification. Do not proceed to frontend implementation.
```

**After sub-agent completes:** Report the design specification to the user.
