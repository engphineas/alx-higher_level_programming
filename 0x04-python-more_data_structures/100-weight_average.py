#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    tuple_prd = 0
    weight_sum = 0

    for tuple_item in my_list:
        tuple_prd += tuple_item[0] * tuple_item[1]
        weight_sum += tuple_item[1]

    return (tuple_item / weight_sum)
