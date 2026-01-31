
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
        self.tail = None 
        self.size = 0
    
    # add value at first
    def add_first(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1
    
    #print list
    def print_list(self):
        current =  self.head
        while current is not None:
            print(current.data, end=("-"))
            current = current.next
        print("None")
    
    # value add at last O(n)
    # def add_last(self,value):
    #     new_node = Node(value)
    #     if self.head is None:
    #         self.head = new_node
    #     else:
    #         current = self.head 
    #         while current.next:
    #             current =  current.next
    #         current.next = new_node
    #     self.size += 1
    
    # optimize way add value at last O(1)
    def add_last_optimize(self, value):
        new_node =  Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1 
    
    # position based add
    def position_based_add(self, data, position):
        if position < 0 or position > self.size:
            return
        if position == 0:
            self.add_first(data)
            return
        if position >= self.size:
            self.add_last_optimize(data)
            return
        new_data = Node(data)
        current = self.head
        for i in range(position - 1):
            current = current.next
        new_data.next =  current.next
        current.next = new_data
        self.size += 1
        
    # search in linked list
    def search_value(self, value):
        current =  self.head
        position = 0
        for i in range(self.size):
            if current.data == value:
                return position
            current = current.next
            position += 1
    
    # delete at first
    def delete_first(self):
        if self.head is None:
            return None
        remove =  self.head.data
        self.head =  self.head.next
        self.size -= 1
        return remove
    
    # delete from last
    def delete_last(self):
        if self.head is None:
            return None
        delated_data = None 
        if self.head.next is None:
            delated_data =  self.head.data
            self.head = None
            self.tail = None
        else:
            current =  self.head
            while current.next.next is not  None:
                current = current.next
            delated_data = current.next.data
            current.next = None
            self.tail = current
        self.size -= 1
        return delated_data          
        
    # delete by position
    def delete_by_postion(self,position):
        if self.head  is None:
            return False
        if position < 0 or position > self.size:
            return False
        
        if position == 0:
            return self.delete_first()
        current =  self.head
        for i in range(position - 1):
            current = current.next
        current.next = current.next.next 
        if position == self.size - 1:
            self.tail = current
        self.size -= 1
        
            
            
            
    

li = LinkedList()
li.add_first(20)
li.add_first(10)
#li.add_last(30)
li.add_last_optimize(30)
li.position_based_add(15, 1)
li.print_list()
print(li.search_value(20))
remove = li.delete_first()
print(remove)
li.print_list()
delete = li.delete_last()
print(delete)
li.print_list()
li.delete_by_postion(1)
li.print_list()
li.delete_by_postion(0)
li.print_list()



        