# The Houseplant Out-of-Office

Entry for make.fun's "The Houseplant Out-of-Office" bounty ($2 in
USDC): the funniest out-of-office auto-reply a houseplant would send,
120 characters or fewer.

## The line

> Thank you for your email. I am currently out of office, out of water, and reconsidering this entire relationship.

(113 characters, one line, within the 1–120 character gate.)

## Why this line

- **Reads as an auto-reply:** "Thank you for your email" opens it,
  and the triple "out of office, out of water, and reconsidering this
  entire relationship" keeps the office format while the plant's life
  takes over.
- **The plant's life drives the joke:** water — or the lack of it —
  is the plant's whole existence, and being ignored for weeks is its
  daily reality.
- **Surprise at the end:** the polite auto-reply collapses into a
  breakup note in the last few words.
- **No office cliches:** no "limited access to email", no "will
  respond on my return" — the reply is the plant giving notice.

## Revision

v1 ended on "Or never", a shrug. v2 gives the plant agency instead:
it is "reconsidering this entire relationship" — a breakup note,
which is a bigger swing than a shrug, and it stays inside the polite
auto-reply format to the last word.

## How to run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR` /
`$MAKEFUN_OUTPUT` if set). Deterministic: the same line every run.
The program asserts the entry is a single line of 1–120 characters
before writing.
