# import implementation
from linked_list import LinkedList
from binary_node import BinaryNode

# # Task 1a
# implementation.month_of_Pi()

# # Task 1b
# implementation.print_favorite_fruits_veggies()

# # Task 1c
# implementation.print_profile()

# # Task 2
# implementation.print_relative_profile()


# Data Structures II
class RunMain:
    def __init__(self) -> None:
        self.my_list = LinkedList()
        self.my_tree = BinaryNode(64)
        
    def append_nodes(self):
        print("\nAdd a new node with the value of 5")
        self.my_list.append_node(5) #pass in an initial value; this method creates a node (and/or sets the head)
        print("\nAdd a new node with the value of 10")
        self.my_list.append_node(10)
        print("\nAdd a new node with the value of 55")
        self.my_list.append_node(55)
        
    def find_values(self):
        print("\nSearch a new node with the value of 10")
        print(self.my_list.find_node(10))
        print("\nSearch a new node with the value of 22")
        print(self.my_list.find_node(22))

# Task 2:
    def insert_binary_values(self):
        print("\n\n === Binary Tree: Insertion Activity===")
        self.data = BinaryNode(77)
        self.data.insert_node(32)
        self.data.insert_node(62)
        self.data.insert_node(89)
        self.data.insert_node(12)
        self.data.insert_node(77)
        self.data.insert_node(61)
        
    # def search_binary_values(self):
    #     print("\nSearch a new node with the value of 32")
    #     self.data.search_for_node(self.data, 32)

if __name__ == '__main__':
    main= RunMain()
    # main.append_nodes() #linked list
    # main.find_values() #linked list
    main.insert_binary_values() #binary search tree
    main.search_binary_values() #binary search tree
            
