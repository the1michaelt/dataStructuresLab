# import implementation
from linked_list import LinkedList
import binary_node

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
        
# RunMain.append_nodes(self)
# RunMain.find_values(self)
 
if __name__ == '__main__':
    main= RunMain()
    main.append_nodes()
    main.find_values()
            
# linked_list.find_node()

# binary_node.insert_node()
        
# binary_node.search_for_node()
