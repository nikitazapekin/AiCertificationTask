flowchart TD
A[Requirements Analyst] -->|Parse requirements, decompose to tasks| B[Brainstorm]
B -->|Structured dialogue to refine ideas into designs| C[Writing Plan]

    subgraph Shared Tasks
        direction LR
        C -->|Create granular implementation tasks| D[Architect]
        D -->|High-level architecture decisions| E[API Designer]
        E -->|Design REST API with Swagger| F[Executing Plans]
        F -->|Manage implementation tasks| G[Using Git Worktrees]
    end

    subgraph Frontend Branch
        direction LR
        G -->|Execute tasks for frontend implementation| H[Frontend Design]
        H -->|Create distinctive, production-grade frontend UI| I[Coder Frontend]
        I -->|Code review for frontend implementation| J[Code Reviewer]
        J -->|Generate unit, integration, E2E tests for frontend| K[Test Generator]
        K -->|Debug frontend issues| L[Systematic Debugger]
        L -->|Finalize frontend branch| M[Finishing Branch]
        M -->|Verification before completion| N[Verification Before Completion]
    end

    subgraph Backend Branch
        direction LR
        G -->|Execute backend implementation tasks| O[Coder Backend]
        O -->|Comprehensive code review including security, performance, architecture| P[Code Reviewer]
        P -->|Generate unit, integration, E2E tests for backend| Q[Test Generator]
        Q -->|Debug backend issues| R[Systematic Debugger]
        R -->|Finalize backend branch| S[Finishing Branch]
        S -->|Verification before completion| T[Verification Before Completion]
    end

    N -->|Generate project-level documentation| U[Documentation Generator]
    T -->|Generate project-level documentation| U

    U -->|Reflect on lessons learned and improve processes| V[Reflect]

    %% Skills Integration
    A -->|Atlassian tools for requirement tracking| W[Atlassian Skill]

