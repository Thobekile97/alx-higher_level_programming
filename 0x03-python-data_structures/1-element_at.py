#!/usr/bin/python3
# 1-element_at.py

def element_at(my_list, idx):
    """
    Retrieve an element from a list.
    """
    if 0 <= idx < len(my_list):
        return my_list[idx]
    return None

# Example usage
my_list = [10, 20, 30, 40, 50]
index = 2
result = element_at(my_list, index)
print("Element at index {}: {}".format(index, result))

