#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary)
    for entry in sorted_dict:
        print("{}: {}".format(entry, a_dictionary[entry]))
