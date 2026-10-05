"""Report whether a short response has been written.

This does NOT grade writing. A short response is read by a person. All this
answers is "has this student written anything yet", which is the one question
an instructor wants before they start reading thirty of them.

It posts the same `marcy/score` status shape the coding assignments use, so
one gradebook script works across both kinds of repo.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

RESPONSE = Path("short_response.md")
PLACEHOLDER = "Your response here"
MIN_WORDS = 40


def words_written(text: str) -> int:
    """Words the student added, with the scaffolding we shipped taken out."""
    body = text
    # Everything above the first "### Response" heading is our scaffolding.
    m = re.search(r"^###\s+Response.*$", body, re.M)
    if m:
        body = body[m.end():]
    body = re.sub(r"```.*?```", " ", body, flags=re.S)
    body = re.sub(r"[#*_>`\[\]()-]", " ", body)
    return len(body.split())


def main() -> None:
    if not RESPONSE.is_file():
        report(0, "short_response.md is missing")
        return

    text = RESPONSE.read_text(encoding="utf-8")
    count = words_written(text)

    if PLACEHOLDER.lower() in text.lower():
        report(0, f"not started ({count} words, placeholder still there)")
    elif count < MIN_WORDS:
        report(0, f"barely started ({count} words)")
    else:
        report(1, f"submitted ({count} words)")


def report(done: int, detail: str) -> None:
    summary = (
        f"## Short response\n\n**{detail}**\n\n"
        + ("Your response is in. Your instructor reads it and replies on your "
           "pull request.\n" if done else
           f"Write your answer in `short_response.md`, replacing the "
           f"`{PLACEHOLDER}...` line. At least {MIN_WORDS} words.\n")
    )
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as f:
            f.write(summary)
    else:
        print(summary)

    repo, sha = os.environ.get("REPO"), os.environ.get("SHA")
    if not (repo and sha):
        return
    subprocess.run(
        ["gh", "api", "-X", "POST", f"repos/{repo}/statuses/{sha}",
         "-f", f"state={'success' if done else 'pending'}",
         "-f", "context=marcy/score",
         "-f", f"description={done}/1 ({done * 100}%) {detail}"[:140]],
        check=False, capture_output=True,
    )


if __name__ == "__main__":
    main()
