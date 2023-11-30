#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    result = 0
    for arguments in sys.argv:
        result += int(arguments)
        print("{}".format(result))
