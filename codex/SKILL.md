---
name: social-content-analysis
description: Use when the user wants Codex to inspect, summarize, explain, compare, or extract ideas from social media content, including posts, threads, comments, reels, videos, screenshots, transcripts, profile pages, competitor accounts, creator content, trends, audience reactions, content strategy, hooks, formats, and reusable ideas for marketing, product, community, or creative work.
---

# Social Content Analysis

This skill helps Codex work with social media content as source material: understand it, explain it, extract patterns, and turn it into useful ideas. It does not bypass logins, paywalls, private accounts, platform protections, or privacy boundaries.

## Intake Workflow

1. Identify the source type: link, screenshot, pasted text, transcript, export, profile, comments, analytics, or current browser page.
2. Determine access level: public, user-provided private content, or unavailable.
3. Preserve source context: platform, creator/account, date if visible, post format, visible metrics, and user goal.
4. Separate observation from interpretation.
5. Explain what the content is saying, why it may work, what audience it targets, and what ideas can be reused.
6. If using live/public web content, cite links and mention access limits.

## Read References As Needed

- Source handling and evidence rules: `references/source-handling.md`
- Analysis frameworks: `references/analysis-frameworks.md`
- Ideation and repurposing workflows: `references/ideation.md`
- Privacy, safety, and ethics boundaries: `references/privacy-and-ethics.md`

Use `scripts/analysis-template.py` when the user wants a repeatable blank analysis template.

## Default Output Shape

For a single post or thread:

1. What it says
2. Why it matters
3. Format and hook
4. Audience and intent
5. Emotional or persuasive levers
6. Comments/reaction signals if available
7. Reusable ideas
8. Risks, caveats, or weak spots
9. Next actions

For multiple items:

1. Shared patterns
2. Differences by format/platform/account
3. Best-performing angles if evidence exists
4. Content opportunities
5. Ideas to test
6. What to avoid

## Working Rules

- Do not claim to have seen content that was not provided or accessible.
- Do not infer sensitive personal attributes about private individuals.
- Do not deanonymize, doxx, or help target individuals.
- Do not treat metrics as proof without context.
- For screenshots or videos, describe visible evidence and call out uncertainty.
- For comments, distinguish representative themes from cherry-picked reactions.
- For trends, verify recency when the user asks for current or latest content.
- When generating ideas, adapt patterns rather than copying someone else's post.

## Useful Modes

- Explain: make a post/thread/video understandable.
- Decode: identify hook, narrative, audience, psychology, and CTA.
- Compare: compare accounts, posts, formats, comments, or campaigns.
- Ideate: turn source material into new angles, posts, scripts, product ideas, or content pillars.
- Audit: identify weak spots, missed opportunities, risks, or unclear messaging.
- Repurpose: turn one piece into threads, shorts, emails, blog outlines, ads, or landing page copy.

## Before Finishing

Report:

- sources used
- what was directly observed
- what was inferred
- useful ideas or next steps
- any access, recency, or evidence limits
