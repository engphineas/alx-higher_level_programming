#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    Max = 0
    for key, score in a_dictionary.items():
        if score > Max:
            Max = score
    for key, score in a_dictionary.items():
        if score == Max:
            return key
