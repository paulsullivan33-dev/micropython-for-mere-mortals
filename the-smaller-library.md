# The Smaller Library

Ask MicroPython what it carries and it will
tell you:

```
$ micropython -c "help('modules')"
__main__          btree             io                select
_asyncio          builtins          json              socket
_thread           cmath             machine           ssl
argparse          collections       math              struct
array             cryptolib         micropython       sys
...
Plus any modules on the filesystem
```

(Excerpted; the lab transcript holds the whole
table, about fifty-five names.) Already the
shape is visible: the everyday core is here —
`os`, `sys`, `time`, `math`, `json`, `re` —
next to things CPython has never heard of
(`btree`, `framebuf`, `uctypes`, `mip`), plus
names with a microcontroller accent.

## The import test

`examples/modules_try.py` tries to import
twenty-three modules and files them under
"imported OK" or "ImportError", under both
interpreters:

```
$ micropython fixtures/modules_try.py
interpreter: micropython (1, 29, 0, '')
imported OK : os, sys, time, math, random, json, re, struct, collections, heapq, socket, select, gc, micropython, machine, array, io, errno, binascii, hashlib
ImportError : itertools, pathlib, threading

$ python3 fixtures/modules_try.py
interpreter: cpython sys.version_info(...)
imported OK : os, sys, ..., itertools, pathlib, threading, ...
ImportError : micropython, machine
```

(CPython's lists are trimmed here; the
transcript has them entire. The pattern is what
matters.)

Read the MicroPython result in three parts:

- **The working core is genuinely working.**
  `json` serialises, `re` matches, `socket` and
  `select` talk to the network on this port,
  `hashlib` hashes. A program that sticks to
  the common core usually runs unchanged —
  chapter 9 proves it with a whole program.
- **Three familiar names are absent.**
  `itertools` (the iterator toolkit),
  `pathlib` (the modern path objects), and
  `threading` (the friendly thread module) do
  not exist. Older MicroPython guides used
  `u`-prefixed names — `uos`, `ujson`, `ure` —
  and those spellings still work on many
  builds, but this one answers to the plain
  CPython names, as the transcript shows.
- **Two names run the other way.**
  `micropython` and `machine` import here and
  fail under CPython. They are MicroPython's
  own additions: chapter 6 takes `micropython`
  apart, and chapter 8 shows what `machine`
  does (and pointedly does not) contain on
  this port.

One absence deserves a footnote: `threading`
is missing, but the module table shows
`_thread`, MicroPython's low-level thread
primitive. Threads exist; the comfortable
CPython interface for them does not. On chip
builds `_thread` itself may be absent — a
variant difference, stated here as
documentation, not measured.

## What to do about a missing module

In order of preference: rewrite around the
core (a list comprehension replaces most
`itertools` habits; string paths replace
`pathlib`), find the MicroPython-native
equivalent (the table is the map), or copy a
pure-Python version of the module onto the
device — modules can also live on the
filesystem, as the help text's last line
hints. What does not work is assuming: run the
import test against *your* build before you
design around a module. Ports and variants
differ, and the test is four lines long.

Check: `micropython -c "import pathlib"` should
fail with `ImportError: no module named
'pathlib'`, and `micropython -c "import json;
print(json.dumps({'a': 1}))"` should print
`{"a": 1}`.
