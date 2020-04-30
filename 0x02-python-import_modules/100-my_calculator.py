#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    la = len(argv)
    if la != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    o = argv[2]
    b = int(argv[3])

    f = {"+": add, "-": sub, "*": mul, "/": div}
    for i in f:
        if o == i:
            print("{:d} {:s} {:d} = {:d}". format(a, o, b, f[i](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
