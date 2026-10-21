# MicroPython for Mere Mortals

**MicroPython** is Python squeezed onto a
microcontroller: a whole programming language
that lives in a few hundred kilobytes on a chip
that costs less than a sandwich, where it reads
sensors, blinks lights, and runs the logic
inside gadgets. It is real Python — the same
language from the series' Python guide — cut
down carefully, not a toy dialect.

This guide teaches it on a computer, not a
chip. MicroPython also builds for ordinary
Linux, Mac, and Windows machines (the **unix
port**), and that build is the lab: big enough
to run everything in these chapters, honest
enough to show where the small Python differs
from the big one.

Every behaviour here was run for real through
**MicroPython v1.29.0** (unix port, standard
build) and cross-checked against **CPython
3.12.3** — the ordinary Python — running the
*same files*. Some chapters are reassuring:
numbers, strings, a whole worked program came
out byte-identical. Some are not: the standard
library is a fraction of the size, a `match`
statement is a syntax error, and memory runs
out in a way you can watch. Both kinds are in
here, with the receipts.

## What this guide covers

- [**What MicroPython is**](what-micropython-is.md) —
  one language, two sizes; the ports, the
  builds, and this guide's two test beds
- [**First steps**](first-steps.md) — the
  REPL, script files, and one-liners: three
  ways to run the same language
- [**The smaller library**](the-smaller-library.md) —
  what `help('modules')` shows, what imports
  fine, and what is simply not there
- [**Numbers**](numbers.md) — big integers,
  floats, and division, run side by side; the
  chapter where the two Pythons refuse to
  differ, and the board caveat that follows
- [**Strings and bytes**](strings-and-bytes.md) —
  f-strings, formatting, and the text/bytes
  split that sensor data forces on you
- [**The micropython module**](the-micropython-module.md) —
  `const`, memory reports, the garbage
  collector, and a heap you can shrink until
  the program says no
- [**Speed decorators**](speed-decorators.md) —
  `@micropython.native` and
  `@micropython.viper`, what they did in this
  build, and one honestly small timing run
- [**Files on this port**](files-on-this-port.md) —
  the real filesystem the unix port sees, and
  the `machine` module that is present but
  has no pins
- [**Worked example: the greenhouse log**](greenhouse-worked-example.md) —
  one complete program, two interpreters, and
  a `diff` that finds nothing
- [**When it breaks**](when-it-breaks.md) —
  the symptom list: missing modules, the
  `match` error, running out of memory, and
  board APIs on the wrong machine
- [**Going to a board**](going-to-a-board.md) —
  what changes on a real microcontroller:
  flashing, pins, buses, and editors —
  labelled documented-only, because none of
  it can run in this lab

## What it doesn't cover

Real hardware. No board was attached to the
lab machine, so everything about pins, I2C,
SPI, flashing a Pico or an ESP32, Thonny, and
WebREPL is described from the documentation
in chapter 11 and marked as such — never
presented as tested. The series' Arduino
guide covers the microcontroller landscape
from the other side. Deep CPython is the
series' Python guide; this one only brings
CPython in as the referee.

## How to use this guide

Read chapters 1–3 in order; they install the
model (one language, a smaller library, a
smaller memory) that explains everything
after. The middle chapters each take one part
of the language and run it against CPython.
Chapter 9 is the proof that ordinary program
logic moves across unchanged, chapter 10 is
the troubleshooting list, and chapter 11 is
the bridge to hardware. Every chapter works
from a file in `examples/`, and the commands
are collected in `examples/commands.txt`, so
you can repeat any capture yourself.
