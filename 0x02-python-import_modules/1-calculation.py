#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    op = ("+", "-", "*", "/")
    fu = (add, sub, mul, div)
    for i in range(4):
        print("{:d} {:s} {:d} = {:d}".format(a, op[i], b, fu[i](a, b)))
