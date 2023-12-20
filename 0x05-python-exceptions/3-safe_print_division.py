#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div_a_b = a / b
    except (ZeroDivisionError):
        div_a_b = None
    finally:
        print("Inside result: {}".format(div_a_b))
        return div_a_b
