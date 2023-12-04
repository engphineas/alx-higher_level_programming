#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_len, tuple_b_len = len(tuple_a), len(tuple_b)
    new_tuple = ((tuple_a[0] if tuple_a_len >= 1 else 0) +
                 (tuple_b[0] if tuple_b_len >= 1 else 0),
                 (tuple_a[1] if tuple_a_len >= 2 else 0) +
                 (tuple_b[1] if tuple_b_len >= 2 else 0))
    return new_tuple
