# data_structures.py

# List data structure
class List:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def insert(self, index, value):
        self.data.insert(index, value)

    def remove(self, value):
        self.data.remove(value)

    def pop(self, index=-1):
        return self.data.pop(index)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __str__(self):
        return str(self.data)

# Tuple data structure
class Tuple:
    def __init__(self, *args):
        self.data = args

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

# Example usage
if __name__ == "__main__":
    my_list = List()
    my_list.append(1)
    my_list.append(2)
    print(my_list)  # Output: [1, 2]

    my_tuple = Tuple(3, 4, 5)
    print(my_tuple)  # Output: (3, 4, 5)
    print(my_tuple[1])  # Output: 4
    print(len(my_tuple))  # Output: 3
