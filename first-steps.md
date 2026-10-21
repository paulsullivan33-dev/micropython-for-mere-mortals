# First Steps

There are three ways to run MicroPython, and
they are the same three as CPython: type at it
interactively, hand it a file, or pass it a
one-liner. On a microcontroller the interactive
way is the famous one — you connect to the chip
and type Python at it live — but it works
identically here, so learn it here.

## The REPL

Start `micropython` with no arguments in a
terminal and you get the **REPL** (read–eval–
print loop), captured from the lab:

```
MicroPython v1.29.0 on 2026-10-21; linux [GCC 13.3.0] version
Type "help()" for more information.
>>> 2 + 3
5
>>> name = "fern"
>>> print(name.upper(), len(name))
FERN 4
>>> import sys
>>> sys.implementation.name
'micropython'
```

Three things to notice. The banner names the
build, as in chapter 1. The prompt is `>>>`,
inherited from CPython. And a bare expression —
`2 + 3`, `sys.implementation.name` — **prints
its value**. That echo belongs to the REPL
only: in a script file, an expression on its
own line computes quietly and prints nothing,
in both Pythons. Half of all beginner confusion
("it worked when I typed it, not in my file")
is exactly this difference.

(The lab captured this through a
pseudo-terminal, because the REPL only appears
when MicroPython is talking to a terminal;
piping lines into it runs them as a script
instead. On your own machine just open a
terminal and type `micropython`.)

## A script file

`examples/first_steps.py` — a station name, five
readings, four summary lines:

```
$ micropython fixtures/first_steps.py
Station: greenhouse
Readings: 5
Warmest: 24.5
Coolest: 18.5
Average: 21.3

$ python3 fixtures/first_steps.py
Station: greenhouse
Readings: 5
Warmest: 24.5
Coolest: 18.5
Average: 21.3
```

Same file, same output, no changes. Most of
this guide is about the cases where that stops
being true — but it is worth starting from the
fact that ordinary Python is ordinary Python.

## One-liners

`micropython -c "..."` runs a snippet directly,
which is how the lab takes most of its
measurements (`-c` is CPython's flag too):

```
$ micropython -c "import sys; print(sys.platform)"
linux
```

Check: `micropython` alone should drop you at a
`>>>` prompt; typing `1 + 1` should answer `2`;
Ctrl-D (or Ctrl-C then Ctrl-D on some systems)
leaves. If instead the program ends immediately
with no prompt, you are not in a terminal —
something piped it.
