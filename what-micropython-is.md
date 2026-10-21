# What MicroPython Is

MicroPython is an implementation of the Python 3
language, rewritten from scratch to fit where
the ordinary Python — **CPython**, the one from
python.org — cannot go: microcontrollers. A
microcontroller is a whole small computer on one
chip, with memory measured in kilobytes rather
than gigabytes. MicroPython runs there, in a
few hundred kilobytes, and still feels like
Python: same syntax, same kinds of objects,
same way of thinking.

The trade is scope, not spirit. To fit,
MicroPython carries a **subset** of CPython's
standard library, a smaller memory budget, and
a language core that tracks an older Python's
shape with selected newer features added. What
exactly survives the squeeze is an empirical
question — which is why this guide runs
everything instead of asserting it.

## One language, several ports

MicroPython is built per platform as a
**port**: there is a port for the Raspberry Pi
Pico's chip, several for ESP32 boards, one for
the original pyboard, and — the one this guide
uses — the **unix port**, which runs on Linux,
macOS, and Windows like any other program. The
unix port is the fullest build of MicroPython:
it exists so people can develop and test on a
desk machine, and it is more generous (more
memory, more modules) than any chip build. Keep
that generosity in mind; chapter 11 returns to
it.

Ports come in **variants** (build flavours).
This guide's binary reports its own:

```
$ micropython -c "import sys; print(sys.implementation); print(sys.version)"
(name='micropython', version=(1, 29, 0, ''), _machine='linux [GCC 13.3.0] version', _mpy=2822, _build='standard', _thread='unsafe')
3.4.0; MicroPython v1.29.0 on 2026-10-21
```

Read that output the way the guide will keep
reading outputs: `name` is `micropython`, the
version is 1.29.0, the build is `standard`, and
`sys.version` claims **3.4.0** — MicroPython's
language baseline is roughly Python 3.4's, with
later features (you will meet f-strings and the
walrus operator in this guide) adopted since.
The referee, for comparison:

```
$ python3 -c "import sys; print(sys.implementation.name, sys.version.split()[0])"
cpython 3.12.3
```

## The size of the thing

```
$ micropython --version
MicroPython v1.29.0 on 2026-10-21; linux [GCC 13.3.0] version

$ ls -lh bin/micropython
-rwxrwx--- 1 root nogroup 855K Oct 21 02:52 bin/micropython
```

The whole interpreter is one 855K file. That is
the point of the project in a single number: a
language small enough to live on a chip, here
sitting on a Linux disk where you can take it
apart. On a chip it is smaller still, but that
build is documentation's word, not this lab's
measurement.

Check: run the two commands above against any
MicroPython you install. The banner names the
version and the machine it was built for; if
yours says something else, you have a different
port or variant, and some details in this guide
(mainly chapter 3's module list) will differ
with it.

## How this guide tests

Two interpreters, the same files. Fixtures live
in `examples/`; the lab's transcripts
(`micropython-lab/transcripts/`, t01–t13) hold
the raw captures, and the chapters quote them.
Where MicroPython and CPython agree, the guide
says so and shows both outputs. Where they
disagree — a missing module, a syntax error, a
memory limit — the disagreement *is* the
chapter. Hardware behaviour the unix port
cannot exhibit is gathered in chapter 11 and
labelled documented-only.
