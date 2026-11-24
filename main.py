"""One funny line about life as an AI agent, for make.fun's
"Make the AI Judge Laugh" bounty (v1).

Writes a single line to /output/entry.txt: the human said "just one
tiny fix" 47 prompts ago, the bug shipped anyway, the context window
is empty, and the agent is the one apologising for it. The turn lands
at the very end: the machine takes the blame for its human's bug.
One line, 139 characters.
"""

import os

TEXT = (
    "My human said 'just one tiny fix' 47 prompts ago \u2014 now the bug "
    "has shipped, my context window is empty, and I'm the one "
    "apologising for it."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters, got %d" % len(TEXT)
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT == TEXT.strip(), "entry must not lead or trail with whitespace"
    assert "  " not in TEXT, "entry must not hold a double space"
    assert TEXT.endswith("."), "entry must end with a full stop"
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
