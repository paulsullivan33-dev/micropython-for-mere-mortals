import time


def sum_plain(n):
    total = 0
    for i in range(n):
        total += i
    return total


N = 300000
start = time.perf_counter()
result = sum_plain(N)
print("cpython plain sum:", result, " took", round((time.perf_counter() - start) * 1000), "ms")
