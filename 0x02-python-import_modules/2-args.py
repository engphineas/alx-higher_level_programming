#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_len = len(sys.argv)
    if args_len == 1:
        print("{} arguments.".format(args_len - 1))
    elif args_len == 2:
        print("{} argument:".format(args_len - 1))
    else:
        print("{} arguments:".format(args_len - 1))
    for arguments in range(1, args_len):
        print("{}: {}".format(arguments, sys.argv[arguments]))
