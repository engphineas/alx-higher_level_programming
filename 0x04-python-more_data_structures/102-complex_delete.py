#!/usr/bin/python3
def complex_delete(my_dict, value):
    temp_dict = my_dict.copy()
    for count, weight in temp.items():
        if value == weight:
            my_dict.pop(count)
    return my_dict
