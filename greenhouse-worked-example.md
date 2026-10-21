# Worked Example: The Greenhouse Log

One complete program, start to finish — the
proof the previous chapters have been pointing
at. `examples/greenhouse.py` analyses a week of
invented greenhouse readings: three
temperatures a day plus an evening
soil-moisture percentage. The gardener's rule:
water in the evening when the day's average
temperature passed 24 degrees **or** the soil
moisture fell below 30%.

The program keeps its data as a list of
tuples, computes each day's average with a
small function, applies the rule with a second
one, prints a table, and finishes with the
week's extremes. Nothing exotic: loops,
format strings, `min`, `max`, `sum`, a list
comprehension. Run under MicroPython:

```
$ micropython fixtures/greenhouse.py
Day  Average  Water?
Mon   20.83   no
Tue   22.67   no
Wed   23.83   YES
Thu   21.83   no
Fri   20.17   no
Sat   24.50   YES
Sun   22.17   no

Week's coolest reading: 16.5
Week's warmest reading: 29.0
Week's average:         22.29
Evenings to water:      2
```

Wednesday earns its YES on dry soil (29%)
despite an average under the heat line;
Saturday earns it on both counts. And now the
referee:

```
$ diff <(micropython fixtures/greenhouse.py) <(python3 fixtures/greenhouse.py)
[exit 0]
```

No output, exit 0: the two interpreters'
answers are **byte-identical**. This is the
fact to build your mental model on. The parts
of Python that describe a problem — data in
tuples and lists, decisions in functions,
results formatted for a human — are the same
language in both implementations. A program
like this one, written on a desk machine under
either interpreter, moves to the other
unchanged.

What would *not* survive the move to an actual
greenhouse controller is everything around the
program: where the readings come from (a
sensor on a pin, not a typed list), where the
table goes (there may be no screen), and how
big the log may grow before chapter 6's heap
says no. The logic transfers; the plumbing is
chapter 11. Keeping those two apart — logic
you can test here, plumbing you must test
there — is the whole working method this
guide is teaching.

Check: change `DRY_SOIL` in the fixture to
`35` and re-run under both interpreters.
Thursday (33%) should join the watering list
in both, and the `diff` should still find
nothing.
