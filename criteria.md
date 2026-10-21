# Writing Criteria

Every guide in this repo is written to the same
standard. If you're adding or editing a guide —
human or AI — hold it to these.

1. **Plain words, real ideas.** Simple language,
   never dumbed-down concepts. Explain jargon on
   first use; collect terms in the glossary.
2. **No hype.** No marketing adjectives, no
   "revolutionary," no promises about what
   something will do for the reader.
3. **Honest about limits.** Say what the thing
   *can't* do. State uncertainty instead of
   smoothing it over. Validation notes include
   what remains unverified.
4. **No invented numbers.** Benchmarks, defaults,
   and specs are either measured or qualified with
   "depends on your setup." If it wasn't tested,
   say so.
5. **Checkable.** Commands are meant to be run,
   with "Check:" blocks showing what success looks
   like. Sources are linked, not asserted.
6. **Respect the reader's setup.** Call out
   Windows/Mac/Linux differences. Don't assume a
   GPU, a budget, or prior experience.
7. **Safety isn't skipped.** Real risks get
   stated plainly, not buried.
8. **Scoped.** Each guide says what it covers and
   points elsewhere for the rest. No guide
   pretends to be the whole subject.
9. **Structure over prose.** Tables, before/after
   examples, symptom → fix. Scannable beats essay.

## Verification notes for this guide

Standard 3 and 4 applied to this guide,
specifically. The interpreters under discussion
are **MicroPython v1.29.0** (unix port, standard
variant, built on the lab machine) and **CPython
3.12.3** (the system `python3`), running the
same fixture files. Working transcripts are kept
with the build (`micropython-lab/transcripts/`,
thirteen files, `t01`–`t13`, produced by the
harness `micropython-lab/run-lab.sh`).

**How the MicroPython binary was obtained —
stated plainly, because the plan changed.**
The guide's first route was a prebuilt Linux
binary from micropython.org. At build time the
site's board-download pages no longer include a
unix download (the unix board page answers
404), so the fallback was used: the official
source, cloned from the project's GitHub at
tag `v1.29.0` (with its submodules), built with
the system GCC 13.3.0 — `mpy-cross`, then
`ports/unix` standard variant. The resulting
binary is 855K and is the interpreter in every
capture. (The GitHub release's `.tar.xz` source
asset was downloaded first, but extracting it
in this sandbox tripped over file-ownership
errors — tar could not set the archived files'
owner and exited in failure, leaving an
incomplete tree that could not build. The git
clone of the same tag is the record that
worked.) The banner's build date, 2026-10-21,
is the lab machine's clock on build day.

**Verified by running, per chapter:**

- *Ch. 1:* `--version` banner;
  `sys.implementation` (version (1, 29, 0),
  `_build` 'standard'); `sys.version` reporting
  3.4.0; the binary's size from `ls -lh`
  (`t01`).
- *Ch. 2:* the REPL, captured through a
  pseudo-terminal (`script -qec`) because the
  REPL only appears on a terminal: banner,
  `>>>` prompts, expression echo (`2 + 3` →
  `5`) (`t02`). The same lines piped as a file
  printed no expression values (observed in
  the lab before the pty capture was made;
  stated as such in the chapter). One script,
  `first_steps.py`, byte-identical output
  under both interpreters (`t03`).
- *Ch. 3:* `help('modules')` entire (~55
  names, quoted as an excerpt), and a 23-name
  import test under both interpreters:
  MicroPython imports 20, missing `itertools`,
  `pathlib`, `threading`; CPython imports all
  but `micropython` and `machine` (`t04`).
- *Ch. 4:* the numbers fixture — outputs
  **identical line for line** under both:
  arbitrary-precision results (`2**100`
  exact), double-precision fingerprints
  (`0.1 + 0.2`), floor division and
  round-half-even agreement (`t05`).
- *Ch. 5:* the strings/bytes fixture —
  identical output under both: f-strings,
  `%` and `.format` styles, bytes indexing
  yielding `115`, in-place `bytearray` edit
  (`t09`).
- *Ch. 6:* `const` values computing as the
  ints they wrap; `micropython.mem_info()`'s
  report (heap total 2072832 on this build);
  `gc.mem_free()` 2071328 after collection;
  `-X heapsize=64k` accepted, startup free
  63616; the allocation fixture dying by
  caught `MemoryError` at 59 KiB blocks in
  the small heap and at 1945 blocks in the
  default heap, then recovering after
  free + collect (`t06`, `t08`). CPython's
  refusal of the same fixture at line 1
  (`t06`).
- *Ch. 7:* `@micropython.native` and
  `@micropython.viper` both present and
  returning 42 (`t07`); the attribute-fetch
  failure — `dir(micropython)` contains
  neither name, `micropython.native` raises
  `AttributeError` — captured in the same
  transcript and explained as compile-time
  spellings. One timing run (`t13`): loop sum
  under 300000, plain 12 ms, native 6 ms,
  viper under the 1 ms tick; CPython plain
  14 ms. Quoted in the chapter as one run of
  a toy loop, which is all it is.
- *Ch. 8:* real-filesystem round trip in a
  scratch dir (write, read, `listdir`,
  `os.stat` as a plain 10-tuple, `remove`);
  `machine`'s unix contents by `dir()`;
  `machine.Pin` raising `AttributeError`
  (`t10`).
- *Ch. 9:* the greenhouse fixture under both
  interpreters, and a `diff` of the two
  outputs exiting 0 with no output (`t11`).
- *Ch. 10:* the walrus fixture running under
  both; the `match` fixture rejected by
  MicroPython with `SyntaxError: invalid
  syntax` at line 2 and run by CPython
  (`t12`); `import pathlib`'s verbatim
  `ImportError: no module named 'pathlib'`
  (also `t04`'s import test).

**Capture hygiene (declared trims):** the REPL
transcript's carriage returns were stripped by
the harness (`tr -d`), declared in `t02`'s
command line itself. Chapter 3 quotes
`help('modules')` as a five-row excerpt and
trims CPython's long import list with marked
ellipses; chapter 8 shortens the `-c` commands'
quoting relative to the harness's escaped form
and marks the `os.stat` tuple's surroundings
in prose rather than reprinting the harness
line. Memory and timing figures are single
captured runs and are quoted as such in place.
No output line was altered.

**Documented-only (not run), and why:**

- *All of chapter 11 — real boards.* No board
  was attached to the lab machine. Flashing
  (UF2 copy, esptool), `boot.py`/`main.py`,
  Thonny, WebREPL, `machine.Pin`/`I2C`/`SPI`/
  `UART`/`PWM`/`ADC` behaviour are described
  from MicroPython's documentation and
  labelled as such in the chapter itself.
- *Constrained-build numbers.* That many
  board builds use small ints without a
  big-integer fallback and single-precision
  floats is stated in chapter 4 from the
  documentation; the lab's build has both
  comforts compiled in and demonstrates the
  opposite behaviour.
- *Board variants of the library.* That
  `_thread` and the network modules vary by
  port/variant is documentation's statement;
  chapter 3's table is this build's, measured.
- *Native/Viper speed on hardware.* The
  chapter-7 timings are the unix build's;
  that the gaps widen on microcontrollers is
  the documentation's expectation, not a
  measurement.
- *The Windows and macOS builds of the unix
  port.* The port targets them; only the
  Linux build was compiled and run here.

Specimen discipline, for the record: every
name, reading, and value in the fixtures is
invented for the guide (a fictional greenhouse
log); no real organisation, system, or person
appears. The lab ran entirely on local files
and one network fetch — the source clone —
with no service or account.
