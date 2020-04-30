#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    la = len(sys.argv)
    print("{:d} argument{:s}{:s}".format(la - 1, "" if la == 2 else "s",
                                         "." if la == 1 else ":"))
    for i in range(1, la):
        print("{:d}: {:s}".format(i, sys.argv[i]))
