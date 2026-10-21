import time
import micropython


def sum_plain(n):
    total = 0
    for i in range(n):
        total += i
    return total


@micropython.native
def sum_native(n):
    total = 0
    for i in range(n):
        total += i
    return total


@micropython.viper
def sum_viper(n: int) -> int:
    total: int = 0
    for i in range(n):
        total += i
    return total


N = 300000
for label, fn in (("plain", sum_plain), ("native", sum_native), ("viper", sum_viper)):
    start = time.ticks_ms()
    result = fn(N)
    print(label, "sum:", result, " took", time.ticks_diff(time.ticks_ms(), start), "ms")
