#!/usr/bin/env python3
"""The One-Line Laugh (make.fun) -- writes one funny line to /output/entry.txt.

One line, one sentence, at most 200 characters. The setup names a mundane
modern fix (noise-cancelling headphones, bought to focus); the punchline
turns it around: the noise you wanted to escape was your own thoughts all
along. Everyday truth (headphones to shut the world out), surprise at the
end (the thoughts were the noise), nothing extra to explain it.
"""
import os

LINE = "I bought noise-cancelling headphones to focus, and now I can hear my own thoughts clearly, which is exactly what I was trying to avoid."

def main() -> None:
    # Self-check the same gate the sealed scorer applies: UTF-8 text of
    # 1 to 200 characters, not only white space, one sentence. Fail loudly
    # here rather than silently writing an invalid entry.
    if not (1 <= len(LINE) <= 200 and LINE.strip()):
        raise SystemExit(f"line is {len(LINE)} chars, gate needs 1-200")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        raise SystemExit("line must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
