# Glossary

**Board** — a microcontroller development
board (Pico, ESP32, pyboard) with MicroPython
installed as its firmware. Chapter 11.

**Build / variant** — a flavour of a port,
compiled with a chosen feature set. This
guide's is the unix port's `standard` variant;
`sys.implementation` reports which one you
have (ch. 1).

**bytearray** — a mutable sequence of bytes;
the buffer type you edit in place (ch. 5).

**bytes** — an immutable sequence of bytes.
Indexing it yields integers, in MicroPython
and CPython alike (ch. 5).

**const** — `micropython.const(x)`: declares
an integer constant the compiler may substitute
inline, saving memory on boards (ch. 6).

**CPython** — the reference implementation of
Python, from python.org; this guide's referee.

**Firmware** — software installed on a chip as
its built-in program. On a board, MicroPython
itself is the firmware (ch. 11).

**Frozen module** — a module compiled into the
firmware/binary itself rather than stored as a
file; several entries in `help('modules')` are
frozen (ch. 3).

**Garbage collector (GC)** — the machinery
that reclaims memory from objects no longer in
use; `import gc` reports and triggers it
(ch. 6).

**Heap** — the memory Python objects are
allocated from. On MicroPython it is a fixed,
settable size (`-X heapsize=` on the unix port)
and running out raises `MemoryError` (ch. 6).

**machine module** — MicroPython's hardware
interface (`Pin`, `I2C`, `ADC`...). Present on
the unix port only as a stub without `Pin`
(ch. 8, 11).

**MemoryError** — the exception raised when
the heap cannot satisfy an allocation;
catchable, and worth rehearsing for (ch. 6).

**MicroPython** — an implementation of
Python 3 written to fit microcontrollers;
a subset of CPython's library with its own
additions (ch. 1, 3).

**mpy-cross** — the cross-compiler that turns
`.py` files into `.mpy` bytecode files ahead of
time, to save memory and startup work on
boards (mentioned in ch. 1's build notes in
the criteria).

**Native emitter** — the compiler path behind
`@micropython.native`, which turns a function
into machine code (ch. 7).

**Port** — a build of MicroPython for one
platform: unix, rp2 (Pico), esp32, and others
(ch. 1).

**REPL** — the read–eval–print loop; the
interactive `>>>` prompt. It echoes expression
values; scripts do not (ch. 2).

**Small int** — a fixed-width integer type
used by constrained builds; past its range a
build without big integers cannot go (ch. 4).

**Unix port** — MicroPython built to run as a
program on Linux, macOS, or Windows; this
guide's lab bench (ch. 1).

**Viper** — the typed, stricter dialect behind
`@micropython.viper`, compiled to machine code
with raw-integer semantics (ch. 7).
