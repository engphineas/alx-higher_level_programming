#!/usr/bin/python3
for num in range(9):
    for i in range(num + 1, 10):
        if num * 10 + i < 89:
            print("{:d}{:d}".format(num, i), end=", ")
print("{:d}".format(89))
