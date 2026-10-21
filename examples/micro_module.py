import micropython
import gc

THRESHOLD = micropython.const(24)


def too_hot(temp):
    return temp > THRESHOLD


print("const at work:", too_hot(26), too_hot(20))
print("threshold type:", type(THRESHOLD))
micropython.mem_info()
gc.collect()
print("gc.mem_free():", gc.mem_free())
print("gc.mem_alloc():", gc.mem_alloc())
print("stack use:", micropython.stack_use())
