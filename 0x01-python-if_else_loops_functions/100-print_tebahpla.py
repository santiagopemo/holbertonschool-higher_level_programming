#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        t = i - 32
    else:
        t = i
    print("{}".format(chr(t)), end="")
