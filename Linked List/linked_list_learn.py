
## Need node propertie- keep data and next node link
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        
"""
new_1 = Node(10)
new_2 = Node(20)
new_3 = Node(30)
print(new_3.data)

# connect nodes
new_1.next = new_2
new_2.next = new_3  ## new_1 - new_2 - new_3
"""

## Create linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0 
        
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    # print linked list
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" - ")
            current = current.next
        print("None")

li = LinkedList()
li.add_first(10)
li.add_first(20)
li.print_list()
           
        
        