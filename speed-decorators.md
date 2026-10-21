# Speed Decorators

MicroPython code on a chip runs slowly compared
to a desktop — the chip is slow, and the
interpreter adds its own cost. MicroPython's
answer is two decorators in the `micropython`
module that compile a chosen function harder.
This build supports both; that is a build
property, so the chapter starts by proving it.

`examples/native_viper.py` decorates one
function each way and calls both:

```
$ micropython fixtures/native_viper.py
native: 42
viper: 42
```

## The two gears

- **`@micropython.native`** compiles the
  function to native machine code instead of
  bytecode. Same Python semantics, fewer
  interpreter steps. It is the low-effort gear:
  decorate, and (mostly) forget.
- **`@micropython.viper`** compiles with a
  stricter, typed dialect: you annotate
  arguments and locals (`a: int`), and in
  return Viper treats them as raw machine
  integers, with pointer operations available
  for board registers. Faster, less forgiving:
  step outside the dialect and the function
  misbehaves or refuses, where plain Python
  would have quietly coped.

Neither exists in CPython — the fixture dies
at `import micropython` there, as chapter 6
showed. Decorated code is therefore
MicroPython-only code; keep it in the small
corner of a program that needs it.

## One small timing run, honestly labelled

`examples/timing.py` sums the integers below
300000 three ways and times each with
`time.ticks_ms()`. One run, on the lab
machine:

```
plain sum: 44999850000  took 12 ms
native sum: 44999850000  took 6 ms
viper sum: 44999850000  took 0 ms
```

And CPython's plain run of the same loop took
14 ms. Read this the way the series reads all
benchmarks: it is **a single run of a toy
loop**, useful for shape, not for promises.
The shapes it does show: all three gears agree
on the answer; native roughly halved this
loop's time; Viper finished below the
millisecond clock's resolution, so the honest
statement is "under a millisecond here", not
a multiplier; and the desktop referee is no
runaway — the interpreted loop cost about the
same in both Pythons on this machine. On a
microcontroller the absolute numbers grow by
orders of magnitude and the gaps between
gears usually grow with them — that scaling
is documentation's claim, not this lab's
measurement, because the lab has no chip.

The working rule: write plain Python first.
Decorate the one hot function the measurements
point at — the sensor loop, the protocol
parser — and leave the rest readable.

One oddity, verified because it looks like a
bug: `native` and `viper` do not exist as
module attributes. `dir(micropython)` lists
`const`, `mem_info`, `stack_use` and friends —
no decorators — and fetching one fails:

```
$ micropython -c "import micropython; f = micropython.native"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'micropython' has no attribute 'native'
```

They are spellings the **compiler** recognises
in decorator position, not functions you can
pass around. So the check for support is never
"go and fetch it" — it is the one this chapter
opened with: decorate a function and run it.

Check: run `examples/native_viper.py`. Two
lines, `native: 42` and `viper: 42`, mean this
build carries both emitters. A build compiled
without them rejects the decorated file
instead — that is the answer to believe.
