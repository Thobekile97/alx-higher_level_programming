#!/usr/bin/python3
def display_sorted_dict(input_dict):
    keys_sorted = list(input_dict.keys())
    keys_sorted.sort()

    for key in keys_sorted:
        print("{}: {}".format(key, input_dict.get(key)))
