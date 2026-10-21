import micropython


@micropython.native
def add_native(a, b):
    return a + b


print("native:", add_native(19, 23))


@micropython.viper
def add_viper(a: int, b: int) -> int:
    return a + b


print("viper:", add_viper(19, 23))
