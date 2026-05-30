# Claude Version

This folder contains the Claude-compatible version of the Social Content Analysis skill.

The Codex version lives in `codex/` and remains optimized for Codex skill conventions. The Claude version lives in `claude/social-content-analysis/` so it can be packaged as a valid Claude skill directory.

## Structure

```text
claude/
└── social-content-analysis/
    ├── SKILL.md
    ├── references/
    │   ├── source-handling.md
    │   ├── analysis-frameworks.md
    │   ├── ideation.md
    │   └── privacy-and-ethics.md
    └── scripts/
        └── analysis-template.py
```

## Packaging For Claude

Claude expects the uploaded ZIP to contain the skill directory, and the directory name should match the `name` field in `SKILL.md`.

Package this folder:

```text
claude/social-content-analysis/
```

The ZIP should look like:

```text
social-content-analysis.zip
└── social-content-analysis/
    ├── SKILL.md
    ├── references/
    └── scripts/
```

## Development Notes

When maintaining the Claude version:

- keep the core concept aligned with the Codex skill
- keep Claude-specific wording in `claude/social-content-analysis/SKILL.md`
- preserve the same privacy and ethics boundaries
- avoid copying Codex-only metadata such as `agents/openai.yaml`
- keep shared analysis concepts consistent across both versions

This branch can be used to develop and review the Claude version before merging it into `main`.
