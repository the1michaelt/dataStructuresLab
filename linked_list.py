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
        value_to_find = new_node
    

    def find_node(self, value_to_find):
        # while current_node.next is not None: #28 minutes into the video
        #     current_node = current_node.next  # move node by node
        while current_node.next is not None: #28 minutes into the video
        # # and find the node that has the value_to_find
        # # if a node has it, return True
        # # if no node has it, return False
        # # self.head.value
        # value_inquiry = value
            if value_to_find == self.head.value:
                return True
            else:
                return False

