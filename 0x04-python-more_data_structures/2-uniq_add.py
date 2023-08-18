#!/usr/bin/python3
def custom_sum(unique_numbers=[]):
    unique_set = set(unique_numbers)
    total = 0

    for num in unique_set:
        total += num

    return total

