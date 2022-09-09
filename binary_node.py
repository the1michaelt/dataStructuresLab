class BinaryNode:
    def __init__(self, key):
        self.data = key #establishes a root value??
        self.left = None  #value less than the root
        self.right = None #value greater than the root
       
    def insert_node(self, key):
        if self.data is None:
            return self.data
        else:
            if self.data == key:
                return self.data
            elif self.data < key:
                self.right= self.right.insert_node(self.right, key)
            else:
                self.left= self.left.insert_node(self.left, key)
        return self.data

    # def search_for_node(self):
    #     pass

        # print("\nInsert a new node with the value of 64")
        # self.my_list.insert_node() #pass in an initial value; this method creates a node (and/or sets the head)
