#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for j in range(list_length):
        try:
            div_lists = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
            div_lists = 0
        except IndexError:
            print("out of range")
            div_lists = 0
        except ZeroDivisionError:
            print("division by 0")
            div_lists = 0
        finally:
            new_list.append(div_lists)
    return new_list
