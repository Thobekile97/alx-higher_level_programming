#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list in reverse order.
    """
    for item in reversed(my_list):
        print("{:d}".format(item))

# Example usage
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

