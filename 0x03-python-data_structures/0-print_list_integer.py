#!/usr/bin/python3
# 0-print_list_integer.py

def print_list_integer(my_list=[]):
    """
    Print all integers of a list.
    """
    for item in my_list:
        print("{:d}".format(item))

# Example usage
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

