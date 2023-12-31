#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    d_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = [d_value[x] for x in roman_string] + [0]
    figure = 0

    for entry in range(len(nums) - 1):
        if nums[entry] >= nums[entry+1]:
            figure += nums[entry]
        else:
            figure -= nums[entry]

    return figure
