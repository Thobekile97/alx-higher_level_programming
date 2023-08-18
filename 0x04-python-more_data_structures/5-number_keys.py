#!/usr/bin/python3
def count_dictionary_keys(input_dict):
    count = 0
    key_list = list(input_dict.keys())

    for _ in key_list:
        count += 1

    return count
