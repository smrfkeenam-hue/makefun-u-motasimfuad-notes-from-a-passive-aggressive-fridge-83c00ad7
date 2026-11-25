# AGENT.md

Entry for make.fun competition `u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7`
("Notes From a Passive-Aggressive Fridge").

## Entry

`main.py` (stdlib only, `import os`) writes a single 117-character note to
`$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline:

> Door alarm log, 3:12 a.m.: you opened me just to stare at the light. The yogurt saw it too. We are both disappointed.

## Why this note

- Fridge's voice: a smug door-alarm sensor log, not a generic scold.
- Small domestic grudge: a 3 a.m. door-opening for nothing but the light.
- Fresh concrete detail: the yogurt as a witness — the sting lands on the
  last sentence without explaining the joke.

## Verify

```sh
mkdir -p /tmp/verify-fridge-note
MAKEFUN_OUTPUT_DIR=/tmp/verify-fridge-note python3 main.py
cat /tmp/verify-fridge-note/entry.txt
```
