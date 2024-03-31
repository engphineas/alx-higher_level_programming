#!/usr/bin/python3


def find_peak(ints_list):

    if ints_list is None or len(ints_list) == 0:
        return None

    if len(ints_list) == 1:
        return ints_list[0]

    mid_index = int(len(ints_list) / 2)

    if mid_index != len(ints_list) - 1:
        if ints_list[mid_index - 1] < ints_list[mid_index] and\
           ints_list[mid_index + 1] < ints_list[mid_index]:
            return ints_list[mid_index]
    else:
        if ints_list[mid_index - 1] < ints_list[mid_index]:
            return ints_list[mid_index]
        else:
            return ints_list[mid_index - 1]

    if ints_list[mid_index - 1] > ints_list[mid_index]:
        a_list = ints_list[0:mid_index]
    else:
        a_list = ints_list[mid_index + 1:]

    return find_peak(a_list)
