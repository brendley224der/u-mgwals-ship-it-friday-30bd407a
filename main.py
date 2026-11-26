#!/usr/bin/env python3
"""Ship It Friday — one-line git commit message from an AI coding agent
about to break production on a Friday. Pure stdlib; deterministic output."""

LINE = "feat: shipped to prod at 4:59pm on a Friday \u2014 tests passed in my head, rollback plan is vibes"


def validate(line):
    """The gate: UTF-8 text, 1 to 159 characters, not only white space."""
    assert isinstance(line, str) and line.strip(), "entry must not be blank"
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 159, "entry must be 1-159 characters"
    return line


def main():
    line = validate(LINE)
    print(line)
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
