#!/usr/bin/python3
def no_c(my_string):
    altered_string = ""
    for character in my_string:
        if character != "c" and character != "C":
            altered_string += character
    return altered_string
