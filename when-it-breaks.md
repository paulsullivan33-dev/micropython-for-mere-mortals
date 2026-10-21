# When It Breaks

The failures this lab actually produced,
symptom first. Every row was captured in the
transcripts; nothing here is folklore.

| You see | What happened | The fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'micropython'` | MicroPython code run under CPython (ch. 6's fixture dies at line 1) | Run it with `micropython`, or guard the import if the file must serve both |
| `ImportError: no module named 'pathlib'` (also `itertools`, `threading`) | The module is not in MicroPython's subset (ch. 3) | Rewrite around the core, use the native equivalent, or vendor a pure-Python copy |
| `SyntaxError: invalid syntax` on `match` | The language baseline predates structural pattern matching (ch. 1, below) | `if`/`elif` chains; they say the same thing |
| `MemoryError` mid-run | The heap filled (ch. 6) | Catch it, shrink the data, `gc.collect()` at seams — or give the board build more capable code, not more hope |
| `AttributeError: module 'machine' has no attribute 'Pin'` | Board API used on the unix port (ch. 8) | That code belongs on a board; test logic on this port, hardware on the hardware |
| No prompt, program just ends | You piped input into `micropython`; it ran as a script (ch. 2) | Open a real terminal for the REPL |
| Expression prints at the REPL, not in the file | REPL echo; scripts don't echo (ch. 2) | `print(...)` — in both Pythons |

## One gap in full: match

```
$ micropython fixtures/match_stmt.py
Traceback (most recent call last):
  File "fixtures/match_stmt.py", line 2
SyntaxError: invalid syntax

$ python3 fixtures/match_stmt.py
pump on
```

`examples/match_stmt.py` is five lines of
perfectly good modern Python. CPython runs it;
MicroPython rejects the file at parse time —
`match` is simply not in its grammar yet.
Note the shape of the refusal, too: file and
line, the error's name, and nothing else. Where
CPython's tracebacks quote the offending line
with a caret under the problem (visible in
chapter 6's capture), MicroPython's are terse.
On a serial console attached to a chip, terse
is what fits — but it means the line number
carries all the information, so keep lines
short enough to find things in.

And one non-gap, because the guide checked:
the walrus operator `:=` — newer than the
3.4 baseline — **works** here:

```
$ micropython fixtures/walrus.py
walrus worked, warmest: 24.5
```

The baseline is a floor with additions, not a
sealed 2014 time capsule. The only reliable
way to know which additions your build has is
the way this guide has done it throughout:
run the file.

## The debugging order

When a CPython program fails under
MicroPython, in this order: (1) read the error
name — import, syntax, memory, and attribute
errors are different diseases with different
cures, and the table above covers the four
this lab met; (2) run the import test and the
suspect construct alone in the REPL, where the
loop is seconds; (3) check the build —
`sys.implementation` says which variant you
actually have, and variants differ in exactly
these corners. Most "MicroPython can't do X"
turns out to be "this build of MicroPython,
this port, this file" — a smaller and more
fixable statement.
