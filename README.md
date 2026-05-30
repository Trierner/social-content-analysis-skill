# Social Content Analysis Skill

A practical AI skill for analyzing social media content, explaining why it works, and turning it into useful ideas.

This repository is designed first for **Codex**, with room to add a **Claude-compatible** version later.

## What It Does

`social-content-analysis` helps an AI assistant work with social media content as source material.

It can analyze:

- public social media links
- screenshots
- pasted posts or threads
- comments and replies
- video or podcast transcripts
- profile pages
- competitor content
- trend examples
- exported analytics or CSVs

And it can help you:

- summarize what the content says
- explain why a post, thread, reel, or video may work
- identify hooks, formats, CTAs, narratives, and audience signals
- extract reusable content patterns
- compare posts, creators, brands, or campaigns
- analyze comment themes and audience reactions
- turn examples into new ideas for posts, scripts, emails, landing pages, products, or campaigns

## Who It Is For

This skill is useful for:

- founders
- marketers
- creators
- product builders
- content strategists
- community builders
- indie hackers
- agencies
- researchers

It is especially helpful when you want to understand *why* content works instead of only collecting examples.

## Important Boundaries

This skill is not a scraper and does not bypass platform rules.

It is designed to work with:

- public content
- content you paste into the chat
- screenshots you provide
- transcripts you provide
- exported data you are allowed to use
- pages opened in a browser session you control

It should not be used to:

- bypass logins, paywalls, or private accounts
- deanonymize users
- collect personal dossiers
- infer sensitive personal attributes
- harass, shame, or target individuals
- copy another creator's content too closely

The goal is to analyze patterns ethically and turn them into original work.

## Repository Structure

```text
social-content-analysis-skill/
├── README.md
├── codex/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   ├── references/
│   │   ├── source-handling.md
│   │   ├── analysis-frameworks.md
│   │   ├── ideation.md
│   │   └── privacy-and-ethics.md
│   └── scripts/
│       └── analysis-template.py
└── claude/
    └── README.md
```

The `codex/` folder contains the Codex skill.

The `claude/` folder is intended for a Claude-compatible version.

## Installing For Codex

Install the Codex skill from the `codex/` folder.

Example:

```bash
python install-skill-from-github.py \
  --repo Trierner/social-content-analysis-skill \
  --path codex \
  --name social-content-analysis
```

After installing, restart Codex so it can pick up the new skill.

## Example Uses

Analyze a post:

```text
Use social-content-analysis to explain why this LinkedIn post works and give me 10 original post ideas based on the same pattern.
```

Analyze comments:

```text
Use social-content-analysis to group these comments into themes, objections, questions, and content opportunities.
```

Repurpose content:

```text
Use social-content-analysis to turn this transcript into a thread, a short-form video script, and a landing page section.
```

Compare competitors:

```text
Use social-content-analysis to compare these three competitor profiles and extract content pillars we could test.
```

## Analysis Modes

The skill supports several working modes:

- **Explain**: summarize and clarify what the content says.
- **Decode**: identify hook, angle, audience, proof, CTA, and persuasive mechanics.
- **Compare**: compare accounts, posts, formats, comments, or campaigns.
- **Ideate**: turn source material into original ideas.
- **Audit**: find weak spots, missed opportunities, and risks.
- **Repurpose**: convert one piece of content into multiple formats.

## Output Style

For a single post or thread, the skill usually looks at:

- what it says
- why it matters
- hook and format
- audience and intent
- emotional or persuasive levers
- comment/reaction signals
- reusable ideas
- caveats or weak spots
- next actions

For multiple pieces of content, it focuses on:

- shared patterns
- differences by format or platform
- possible winning angles
- content opportunities
- ideas to test
- what to avoid

## Codex vs Claude

This repository is currently built for **Codex**.

Adding a `claude/` folder is intentional: each assistant has slightly different skill conventions and trigger behavior.

Recommended approach:

- Keep the shared concept and references aligned.
- Adapt the instructions for each assistant.
- Avoid one generic skill that tries to serve every runtime equally.
- Keep platform-specific files in their own folders.

## License

Choose a license before publishing widely.

For public reuse, MIT is simple and permissive.
