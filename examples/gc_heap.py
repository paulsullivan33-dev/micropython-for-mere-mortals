import gc

blocks = []
try:
    while True:
        blocks.append(bytearray(1024))
except MemoryError:
    print("MemoryError after allocating", len(blocks), "one-KiB blocks")

print("still alive; freeing the list and collecting")
blocks = None
gc.collect()
print("gc.mem_free() now:", gc.mem_free())
