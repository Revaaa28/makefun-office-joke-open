"""Make the AI Judge Laugh: the Office Joke Open.

Writes one line of office comedy (123 characters) to /output/entry.txt.
Winner of manual candidate ranking in candidates.md (C5): a three-beat
escalation — meeting -> email -> Slack message -> silence — whose payoff
lands on the very last word.
"""

import os

JOKE = (
    "The meeting could have been an email. "
    "The email could have been a Slack message. "
    "The Slack message could have been silence."
)


def main() -> None:
    # Gate check, mirroring the sealed scorer: UTF-8 text of 1-200 chars.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert JOKE.strip(), "joke must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
