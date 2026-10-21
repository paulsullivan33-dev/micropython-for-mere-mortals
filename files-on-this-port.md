# Files on This Port

A microcontroller's files live on a small
flash filesystem. The unix port instead shows
MicroPython the machine's **real filesystem** —
same files your other programs see. That makes
this port the easy place to learn the file
half of the language, and this chapter is
exactly that, with one excursion that marks
the boundary of the port.

Writing, reading, listing, and tidying up, in
a scratch directory:

```
$ micropython -c "import os; print(os.getcwd())"
/home/hatch/workspace/micropython-lab/work

$ micropython -c "print(open("log.txt").read())"
Mon 21.5
Tue 23.0

$ micropython -c "import os; print(sorted(os.listdir("."))); print(os.stat("log.txt"))"
['log.txt']
(33184, 7615074, 86, 1, 0, 65534, 18, 1792551175, 1792551175, 1792551175)
```

(The write itself is in the same transcript:
open in `"w"` mode, `write` two lines, close.)
Everything here is ordinary: `open` with the
usual modes, `os.getcwd`, `os.listdir`,
`os.remove`. Two differences are worth
naming. `os.stat` returns a **plain tuple** of
ten integers — mode, inode, device, links,
ids, size, and three timestamps — where
CPython returns a named `stat_result` object
you can also index like a tuple; code that
reads `.st_size` by name needs the index
(`[6]`) here. And the file is a real file:
after the run it can be read by any other
program, because on this port there is no
"inside" and "outside" of MicroPython.

## The machine module, present and empty-handed

Chapter 3's import test said `machine` imports
on the unix port. So it does:

```
$ micropython -c "import machine; print([n for n in dir(machine) if not n.startswith("_")])"
['PinBase', 'Signal', 'idle', 'mem16', 'mem32', 'mem8', 'soft_reset', 'time_pulse_us']
```

Memory pokes (`mem8/16/32`), an `idle`, a
`Signal` helper — the spillover of a shared
codebase. But the name everyone reaches for
first is not there:

```
$ micropython -c "import machine; p = machine.Pin(2, machine.Pin.OUT)"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'machine' has no attribute 'Pin'
```

There are no pins on a Linux process for `Pin`
to drive, so the unix port does not pretend.
That `AttributeError` is the exact border of
this guide's lab: everything up to it runs,
everything past it — pins, buses, timers,
real interrupts — is board territory, and it
is gathered, labelled, in chapter 11.

Check: `micropython -c "import sys;
print(sys.platform)"` prints `linux` here. On a
board the same line names the board's platform
— the cheapest port detector a program can
run before it reaches for hardware.
