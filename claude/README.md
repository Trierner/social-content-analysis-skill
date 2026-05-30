# Claude Version

This folder is reserved for a Claude-compatible version of the Social Content Analysis skill.

The Codex version lives in `codex/` and should remain optimized for Codex skill conventions.

## Development Notes

When building the Claude version:

- adapt the instructions to Claude's skill format and invocation behavior
- keep the core concept aligned with the Codex skill
- preserve the same privacy and ethics boundaries
- avoid copying runtime-specific metadata that only Codex uses
- keep shared analysis concepts consistent across both versions

## Planned Structure

```text
claude/
├── SKILL.md
├── references/
│   ├── source-handling.md
│   ├── analysis-frameworks.md
│   ├── ideation.md
│   └── privacy-and-ethics.md
└── scripts/
    └── analysis-template.py
```

This branch can be used to develop and review the Claude version before merging it into `main`.
