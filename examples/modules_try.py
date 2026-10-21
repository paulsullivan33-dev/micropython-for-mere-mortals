import sys

candidates = [
    "os", "sys", "time", "math", "random", "json", "re", "struct",
    "collections", "heapq", "itertools", "pathlib", "threading",
    "socket", "select", "gc", "micropython", "machine", "array",
    "io", "errno", "binascii", "hashlib",
]

ok = []
missing = []
for name in candidates:
    try:
        __import__(name)
        ok.append(name)
    except ImportError:
        missing.append(name)

print("interpreter:", sys.implementation.name, sys.implementation.version)
print("imported OK :", ", ".join(ok))
print("ImportError :", ", ".join(missing))
