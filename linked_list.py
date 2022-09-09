class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
       

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, value_to_add):
        new_node = Node(value_to_add)        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
   
     
    def find_node(self, value_to_find):
        current_node = self.head.value #Starting point 
        while current_node is not None: # while there is another node; 28 minutes into the video
        # move node by node. As long as next is not empty
        # # self.head.value
            if value_to_find != self.head.value: #returns true on any value that is not the head
                return True  # # if a node has it, return True
            else:
                return False # # if no node has it, return False
        current_node = current_node.next

