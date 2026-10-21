# The micropython Module

One module in the table is MicroPython's own:
`micropython`, the door to the implementation
itself. Under CPython it does not exist —
running this chapter's fixture there ends at
line 1:

```
$ python3 fixtures/micro_module.py
Traceback (most recent call last):
  ...
ModuleNotFoundError: No module named 'micropython'
```

Under MicroPython, `examples/micro_module.py`
shows its three everyday faces.

## const: saying "this never changes"

`micropython.const(24)` declares an integer
constant. In the run it behaves as the integer
it wraps:

```
const at work: True False
threshold type: <class 'int'>
```

The point is invisible on the unix port and
matters on boards: the compiler may substitute
the value wherever the name appears, saving
the memory a global variable would cost. (The
substitution itself is a compiler behaviour,
stated from the documentation; what the lab
measured is that `const` values compute and
compare exactly like the integers they wrap.)

## mem_info: asking the memory how it is

```
mem: total=6117, current=1695, peak=4046
stack: 896 out of 80000
GC: total: 2072832, used: 1888, free: 2070944
```

`micropython.mem_info()` prints a report:
Python-object memory (total/current/peak),
the stack, and the garbage collector's heap —
here about **2 megabytes** total with nearly
all of it free. Two companion functions give
the same story as numbers a program can act
on: after a collection, the fixture read
`gc.mem_free()` as 2071328 and
`gc.mem_alloc()` as 1504. (Exact figures move
from run to run; the transcript is one
captured run, and yours will differ in detail,
not in shape.)

## A heap you can shrink

Memory on a board is fixed and small, and
programs die of it. The unix port lets you
rehearse that death: `-X heapsize=` sets the
heap before the program starts.

```
$ micropython -X heapsize=64k -c "import gc; gc.collect(); print("mem_free at startup:", gc.mem_free())"
mem_free at startup: 63616

$ micropython -X heapsize=64k fixtures/gc_heap.py
MemoryError after allocating 59 one-KiB blocks
still alive; freeing the list and collecting
gc.mem_free() now: 63040
```

`examples/gc_heap.py` allocates one-kilobyte
blocks until the interpreter refuses. In a
64 KB heap it got 59, raised `MemoryError` —
which the program **caught**, so it could free
its list, collect, and report 63040 bytes free
again. With the default heap the same file
reached 1945 blocks before the same refusal.
Two lessons generalise: exhaustion is a
catchable event, not a crash, if you write the
`except MemoryError` before you need it; and
the distance between "works on my desk build"
and "works on the device" is often just this
number. Rehearse with a shrunken heap before
the hardware teaches you the same lesson less
politely.

Check: `micropython -X heapsize=64k -c "import
gc; print(gc.mem_free())"` should print a
number under 65536; without the `-X`, a number
in the millions on this build.
