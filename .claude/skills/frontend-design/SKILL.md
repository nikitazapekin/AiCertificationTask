---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use when designing user interfaces, creating UI specifications, or styling web components. Triggers on "frontend design", "UI design", "user interface", "UX design", "style", "beautify". Generates creative, polished design that avoids generic AI aesthetics.
---

# Frontend Design

Create distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Focus on exceptional attention to aesthetic details and creative choices that make interfaces memorable.

## Design Thinking Process

Before any implementation, understand the context and commit to a BOLD aesthetic direction:

### 1. Understand Context

- **Purpose**: What problem does this interface solve? Who uses it?
- **Audience**: Technical users, general consumers, enterprise, creative professionals?
- **Brand**: Does it need to match existing brand guidelines or is it greenfield?
- **Constraints**: Technical requirements (framework, performance, accessibility)

### 2. Choose Aesthetic Direction

Pick a clear conceptual direction and execute with precision. Options include:

| Direction              | Characteristics                                                  |
| ---------------------- | ---------------------------------------------------------------- |
| Brutally Minimal       | Maximum whitespace, essential elements only, stark contrasts     |
| Maximalist Chaos       | Dense information, overlapping elements, controlled visual noise |
| Retro-Futuristic       | Vintage sci-fi aesthetics, CRT effects, terminal vibes           |
| Organic/Natural        | Soft curves, nature-inspired colors, flowing layouts             |
| Luxury/Refined         | Premium materials, subtle animations, restrained elegance        |
| Playful/Toy-like       | Bright colors, bouncy animations, game-inspired elements         |
| Editorial/Magazine     | Strong typography hierarchy, grid-based, print-inspired          |
| Brutalist/Raw          | Exposed structure, unconventional layouts, anti-design           |
| Art Deco/Geometric     | Strong shapes, metallic accents, symmetrical patterns            |
| Industrial/Utilitarian | Functional-first, muted tones, no-nonsense clarity               |

**CRITICAL**: Bold maximalism and refined minimalism both work - the key is **intentionality**, not intensity.

### 3. Define Differentiation

Ask: What makes this UNFORGETTABLE? What's the one thing someone will remember?

## Aesthetic Guidelines

### Typography

**DO:**

- Choose fonts that are beautiful, unique, and interesting
- Pair a distinctive display font with a refined body font
- Use unexpected, characterful font choices that elevate the design
- Create clear hierarchy through size, weight, and spacing

**NEVER:**

- Default to generic fonts: Inter, Roboto, Arial, system fonts
- Use the same overused "safe" choices (Space Grotesk, etc.)
- Ignore font pairing - display and body fonts should complement

### Color & Theme

**DO:**

- Commit to a cohesive palette that matches the aesthetic direction
- Use CSS variables for consistency
- Apply dominant colors with sharp accents
- Vary between light and dark themes across designs

**NEVER:**

- Use timid, evenly-distributed palettes
- Default to cliché schemes (purple gradients on white backgrounds)
- Choose safe, forgettable color combinations

### Motion & Animation

**DO:**

- Focus on high-impact moments: orchestrated page load with staggered reveals
- Use scroll-triggering and hover states that surprise
- Create micro-interactions that delight
- Prefer CSS-only solutions for HTML, Motion library for React

**NEVER:**

- Scatter random animations without purpose
- Use generic fade-ins everywhere
- Ignore the timing and easing curves (they matter!)

### Spatial Composition

**DO:**

- Explore unexpected layouts: asymmetry, overlap, diagonal flow
- Use grid-breaking elements intentionally
- Apply generous negative space OR controlled density (match the aesthetic)
- Create visual rhythm through spacing patterns

**NEVER:**

- Default to predictable grid-only layouts
- Use cookie-cutter component patterns
- Ignore the relationship between elements

### Backgrounds & Visual Details

**DO:**

- Create atmosphere and depth (not just solid colors)
- Add contextual effects that match the aesthetic:
  - Gradient meshes, noise textures, geometric patterns
  - Layered transparencies, dramatic shadows
  - Decorative borders, custom cursors, grain overlays
- Use these elements to reinforce the design direction

**NEVER:**

- Leave backgrounds as flat solid colors by default
- Add effects that contradict the chosen aesthetic
- Use generic gradients without purpose

## Anti-Patterns: AI Slop to Avoid

These are signs of generic, forgettable AI-generated design:

- ❌ Overused font families (Inter, Roboto, Arial)
- ❌ Purple-to-blue gradients on white backgrounds
- ❌ Rounded rectangles with drop shadows everywhere
- ❌ Predictable card-based layouts
- ❌ Generic hero sections with stock-photo-style imagery
- ❌ Cookie-cutter component patterns
- ❌ Safe, forgettable color choices
- ❌ No context-specific character

## Design Deliverables

When creating a design specification:

```markdown
# [Feature] Frontend Design

## Aesthetic Direction

[Chosen direction and rationale]

## Key Design Decisions

- Typography: [Fonts and hierarchy]
- Color Palette: [Primary, secondary, accent colors]
- Motion: [Animation strategy]
- Layout: [Spatial approach]

## Memorable Element

[The one thing that makes this unforgettable]

## Component Visual Specs

[For each key component: visual description, states, interactions]

## Responsive Behavior

[How the design adapts across breakpoints]
```

## Quality Standard

Match implementation complexity to the aesthetic vision:

- **Maximalist designs** need elaborate code with extensive animations and effects
- **Minimalist designs** need restraint, precision, and careful attention to spacing, typography, and subtle details

Elegance comes from executing the vision well.

**Remember**: Claude is capable of extraordinary creative work. Don't hold back - show what can truly be created when thinking outside the box and committing fully to a distinctive vision.

---

## Next Steps

After frontend design is complete, STOP and present these options:

**Next by flow:** `/coder-frontend [context]` - Implement the designed UI components.

**Alternatives:**
- `/brainstorm [context]` - Further refine the design through dialogue.
- `/architect [context]` - Review frontend architecture decisions.
