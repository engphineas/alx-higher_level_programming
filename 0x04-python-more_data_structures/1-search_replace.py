#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_new = list(my_list)
    for value in range(len(list_new)):
        if list_new[value] == search:
            list_new[value] = replace
    return list_new
