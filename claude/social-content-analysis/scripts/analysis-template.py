#!/usr/bin/env python3
"""Print a reusable social content analysis template."""

from __future__ import annotations


TEMPLATE = """# Social Content Analysis

## Source

- Platform:
- Account/creator:
- URL or source type:
- Date visible:
- Format:
- User goal:

## Observed

- Core message:
- Hook:
- Visual/audio elements:
- CTA:
- Visible metrics:
- Comment themes:

## Inferred

- Intended audience:
- Audience pain/desire:
- Emotional levers:
- Why it may work:
- Weak spots:

## Ideas

- Reusable pattern:
- Adaptation 1:
- Adaptation 2:
- Adaptation 3:
- What to avoid copying:

## Next Actions

- Verify:
- Test:
- Produce:
"""


def main() -> int:
    print(TEMPLATE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
