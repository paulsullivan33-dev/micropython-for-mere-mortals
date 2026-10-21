# Strings and Bytes

If numbers were the chapter where the two
Pythons refused to differ, strings are the
chapter where they agree about the thing that
actually matters on a microcontroller: the
split between **text** (`str`) and **bytes**
(`bytes`, `bytearray`). Sensor readings,
network packets, and serial lines are bytes;
words on a screen are text; confusing them is
the standard beginner bug in both languages,
and MicroPython keeps the same rules.

`examples/strings_bytes.py` runs the everyday
operations; both interpreters produced this,
identically:

```
An f-string: the fern has 6 fronds
Percent style: fern is 42 cm tall
Formatted float: 3.14
bytes: b'soil:OK'  first byte: 115
bytearray after edit: bytearray(b'fan:on ')
split: ['Water', 'Rest', 'Shade']
upper: GREENHOUSE
joined: a-b-c
slice: green house
```

What to take from it:

- **All three formatting styles work.**
  f-strings (a post-3.4 feature MicroPython
  adopted — remember the `3.4.0` baseline from
  chapter 1 is a floor, not a ceiling),
  `"{}".format(...)`, and `%` formatting all
  produced the same lines in both
  interpreters.
- **Indexing bytes gives an integer.** The
  first byte of `b"soil:OK"` is `115` — the
  code for `s` — not a one-byte string. Code
  that reads a sensor's reply byte by byte
  depends on this, and it matches CPython.
- **`bytearray` is the mutable one.** The
  fixture rewrites `fan:off` into `fan:on ` in
  place — the pattern behind building a
  message buffer without making new strings,
  which is how you behave when memory is
  counted in kilobytes (chapter 6).
- **The string method kit is present.**
  `split`, `upper`, `join`, slicing — nothing
  in the run surprised either interpreter.

The honest limit is breadth, not behaviour:
CPython's `str` carries a longer tail of
methods and the `re` module a longer tail of
features than MicroPython's subset. The
fixture deliberately uses the common core;
code that reaches for an obscure method
should be import-tested and run-tested
against the target build, the same advice as
chapter 3.

Check: `micropython -c "print(b'fan'[0])"`
should print `102` (the code for `f`), and
the same under `python3`. If a build ever
answered with a byte string instead, every
byte-reading loop you own would need
rethinking — which is why the check is worth
the ten seconds.
