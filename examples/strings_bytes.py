name = "fern"
print(f"An f-string: the {name} has {6} fronds")
print("Percent style: %s is %d cm tall" % ("fern", 42))
print("Formatted float: {:.2f}".format(3.14159))

data = b"soil:OK"
print("bytes:", data, " first byte:", data[0])
mutable = bytearray(b"fan:off")
mutable[4:] = b"on "
print("bytearray after edit:", mutable)

text = "Water,Rest,Shade"
print("split:", text.split(","))
print("upper:", "greenhouse".upper())
print("joined:", "-".join(["a", "b", "c"]))
print("slice:", "greenhouse"[0:5], "greenhouse"[-5:])
