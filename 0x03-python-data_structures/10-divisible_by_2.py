#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    if my_list:
        for number in my_list:
            if number % 2 == 0:
                resulting_list.append(True)
            else:
                resulting_list.append(False)
        return resulting_list
