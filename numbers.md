# Numbers

This is the chapter where the guide went
looking for differences and mostly did not
find them — which is itself the finding, and
worth stating carefully, because the *next*
machine you run this code on may differ where
this one does not.

`examples/numbers.py` pokes at the usual
pressure points: the biggest machine integer,
powers far beyond it, a long multiplication,
the famous `0.1 + 0.2`, a third, floor division
and remainder with a negative, and rounding
halves. MicroPython's output:

```
maxsize: 9223372036854775807
10**30 = 1000000000000000000000000000000
2**100 = 1267650600228229401496703205376
123456789 * 987654321 = 121932631112635269
0.1 + 0.2 = 0.30000000000000004
repr(1/3) = 0.3333333333333333
7 // 2 = 3  -7 // 2 = -4
7 % 2 = 1  -7 % 2 = 1
round(2.5) = 2  round(3.5) = 4
```

CPython's output for the same file is in the
same transcript, and it is **identical, line
for line**. Take the results one at a time:

- **Integers do not overflow here.** `2**100`
  comes out exact. This unix build uses
  arbitrary-precision integers (the "long int"
  implementation is compiled in), so past
  `sys.maxsize` the numbers just get bigger
  and slower, exactly as in CPython.
- **Floats are doubles.** `0.1 + 0.2` produces
  the same `0.30000000000000004` fingerprint
  and `1/3` the same sixteen digits — the
  fingerprint of 64-bit floating point, shared.
- **The rounding rules match.** Floor division
  floors (`-7 // 2` is `-4`, not `-3`), the
  remainder takes the divisor's sign, and
  `round` rounds halves to even (`round(2.5)`
  is `2`). These are language rules, and the
  small Python keeps them.

## The caveat that matters

All of that is a property of **this build**,
not of MicroPython everywhere. The numbers
story is a build-time choice: many
microcontroller builds use 30-bit small
integers with no big-integer fallback, and
single-precision (32-bit) floats — because
RAM is precious and the code must fit. On
such a board, `10**30` fails or wraps (build
dependent) and `1/3` prints fewer digits.
That behaviour is stated here from the
documentation; the lab has no board to
measure it on.

So the rule for portable code: do your
arithmetic on the unix port to develop it,
but treat exact integer range and float
precision as things to **verify on the
target**, not to assume. If a program's
correctness depends on `2**100` being exact
or on the sixteenth digit of a third, it is
relying on build options, not on the
language — and it should say so in a comment.

Check: run `examples/numbers.py` under any
other Python you have. Every line should match
the block above except, on a constrained
build, the big-integer and float lines — and
now you know which lines to look at first.
