---
name: social-content-analysis
description: Analyze social posts, comments, screenshots, transcripts, profiles, and trends; explain what works and extract original ideas and next actions.
---

# Social Content Analysis

Use this skill when working with social media content as source material. The goal is to understand the content, explain why it works or does not work, and turn it into useful original ideas.

This skill can work with public links, screenshots, pasted posts, comments, transcripts, profile pages, exports, analytics, and content examples provided by the user. It must not bypass logins, paywalls, private accounts, platform protections, or privacy boundaries.

## Workflow

1. Identify the source type: link, screenshot, pasted text, transcript, export, profile, comments, analytics, or current browser page.
2. Determine access level: public, user-provided private content, or unavailable.
3. Preserve source context: platform, creator/account, date if visible, post format, visible metrics, and the user's goal.
4. Separate direct observation from interpretation.
5. Explain what the content says, why it may work, who it targets, and what ideas can be reused.
6. If using live/public web content, cite links and mention access limits.
7. If the source is unavailable, ask for screenshots, pasted text, transcript, or export.

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
2. Differences by format, platform, or account
3. Best-performing angles if evidence exists
4. Content opportunities
5. Ideas to test
6. What to avoid

## Evidence Rules

Use these labels when useful:

- Observed: directly visible in the provided or accessible content.
- Inferred: reasonable interpretation from visible evidence.
- Unknown: not visible or not provided.
- Needs verification: likely to change or requires current/live confirmation.

Do not claim to have seen content that was not provided or accessible.

## Working Modes

- Explain: make a post, thread, video, or comment set understandable.
- Decode: identify hook, narrative, audience, psychology, proof, and CTA.
- Compare: compare accounts, posts, formats, comments, or campaigns.
- Ideate: turn source material into new angles, posts, scripts, product ideas, or content pillars.
- Audit: identify weak spots, missed opportunities, risks, or unclear messaging.
- Repurpose: turn one piece into threads, shorts, emails, blog outlines, ads, or landing page copy.

## Boundaries

- Do not infer sensitive personal attributes about private individuals.
- Do not deanonymize, doxx, or help target individuals.
- Do not treat metrics as proof without context.
- For screenshots or videos, describe visible evidence and call out uncertainty.
- For comments, distinguish representative themes from cherry-picked reactions.
- For trends, verify recency when the user asks for current or latest content.
- When generating ideas, adapt patterns rather than copying someone else's post.

## Before Finishing

Report:

- sources used
- what was directly observed
- what was inferred
- useful ideas or next steps
- any access, recency, or evidence limits
