"""The Houseplant Out-of-Office — the funniest out-of-office
auto-reply a houseplant would send, 120 characters or fewer.

REVISION (v1 -> v2): the v1 line ended on "Or never", a shrug. The v2
line gives the plant agency instead: it is "reconsidering this entire
relationship". The plant's life still drives the joke — out of office,
out of water — but the punch is now a breakup note, which is a bigger
swing than a shrug, and it stays inside the polite auto-reply format
to the last word.
"""

import os

LINE = (
    "Thank you for your email. I am currently out of office, out of "
    "water, and reconsidering this entire relationship."
)

assert 1 <= len(LINE) <= 120, len(LINE)
assert "\n" not in LINE.strip()

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT") or "/output"
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
print(f"wrote entry ({len(LINE)} chars)")
