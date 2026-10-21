# Going to a Board

**Everything in this chapter is
documented-only.** No board was attached to
the lab machine; nothing here was run. It is
written from MicroPython's documentation so
the previous ten chapters have somewhere to
land, and so you know exactly which of their
lessons transfer and which stop at the lab
door. Where this chapter and a capture ever
disagree, believe the capture.

## What a board is, in this guide's terms

A **board** — a Raspberry Pi Pico, an ESP32
development board, the original pyboard — is a
microcontroller with MicroPython installed as
its **firmware**: the interpreter *is* the
operating system. There is no Linux under it,
no shell next to it. The board runs your
program the way this guide's unix port runs a
file, except the "file" is transferred onto
the chip and the machine it runs on has
kilobytes-to-megabytes of memory instead of
this port's comforts.

**Getting MicroPython onto one** (from the
documentation): each board's download page on
micropython.org offers a firmware file. Pico-
family boards appear as a USB drive when
booted with their button held, and you copy a
`.uf2` file onto it. ESP32 boards are written
over serial with a tool called `esptool`.
After that the board reboots into MicroPython
and offers the same `>>>` REPL from chapter 2 —
over a USB serial connection, which is why
that chapter's skill is the first one worth
having.

**Talking to it.** Three documented routes:
a terminal program over the serial line (the
REPL, raw); **Thonny**, a beginner-friendly
Python editor that speaks to boards directly —
browse the board's files, edit, run, see the
REPL in the same window; and **WebREPL**, a
REPL in a browser tab served by the board
itself over Wi-Fi, on boards that have Wi-Fi.
Two filenames have conventions: `boot.py`
runs first at power-up, `main.py` runs after
it — put your program in `main.py` and the
board runs it whenever it powers on.

## The hardware half of the language

What waits on a board, all under the `machine`
module whose unix-port stub you met in
chapter 8:

- **`machine.Pin`** — a physical pin as an
  object: set it as input or output, read or
  write its level. The first line of a hundred
  thousand tutorials, and the line that raised
  `AttributeError` here.
- **Buses** — `machine.I2C`, `machine.SPI`,
  `machine.UART`: the three standard ways
  chips talk to sensors, displays, and each
  other.
- **Timing and touch** — `machine.PWM` for
  dimming and servos, timers, and the ADC
  (`machine.ADC`) that turns a voltage into a
  number: where chapter 9's typed-in readings
  actually come from.

## What transfers, and what does not

**Transfers unchanged** — proven, not hoped:
the language core as far as this guide tested
it (chapters 4, 5, 9), the smaller-library map
(chapter 3, modulo the target build's own
variant), the `micropython` module's habits —
`const`, `gc` discipline, catching
`MemoryError` (chapter 6) — and the working
method: develop the logic here, rehearse it
under a shrunken heap, *then* carry it over.

**Does not transfer, or transfers smaller:**
the filesystem (a board's flash is small and
its `os` is thinner — no `getcwd` into a deep
tree, no gigabytes of logs); the numbers
headroom (chapter 4's caveat: small ints and
single-precision floats are common board
choices); the generous module table (network
modules exist only where the hardware and
build include them); and every line that
touches `machine` — there is no substitute for
running it on the board it will live on.

That is the honest shape of the subject: one
language, learned properly on a machine that
can show you its workings, and a final step —
the hardware — that no amount of desk testing
replaces. The desk work still earns its keep:
it is where the logic stops being wrong.
