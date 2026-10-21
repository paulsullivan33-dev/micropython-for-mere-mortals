# A first script: the same file runs under MicroPython and CPython.
name = "greenhouse"
readings = [18.5, 21.0, 24.5, 23.0, 19.5]

print("Station:", name)
print("Readings:", len(readings))
print("Warmest:", max(readings))
print("Coolest:", min(readings))
print("Average:", sum(readings) / len(readings))
