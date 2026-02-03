
class Node:
    def __init__(self, data=0, next=None):
        self.data = data  
        self.next = next 

class Linkedlist:
    def __init__(self):
        self.head_dummy =  Node()
        self.size = 0
    
    def get(self, index):
        if index < 0 or index >= self.size:
            return
        current = self.head_dummy.next
        for _ in range(index):
            current =  current.next
        return current.data 
    
    def addAtFirst(self,val):
        self.insert_at_index(0,val)
        
    def addAtTail(self, val):
        self.insert_at_index(self.size, val)
        
    def insert_at_index(self, index, val):
        if index < 0 or index > self.size:
            return
        prev = self.head_dummy
        for i in range(index):
            prev = prev.next
        new_node = Node(val)
        new_node.next = prev.next
        prev.next = new_node
        self.size += 1
    
    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            return
        prev = self.head_dummy
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.size -= 1
        
    def print_list(self):
        current = self.head_dummy.next
        while current:
            print(current.data, end="-")
            current = current.next
        print('None')

li = Linkedlist()
li.addAtFirst(10)
li.addAtFirst(5)
li.insert_at_index(1, 15)
li.delete_at_index(1)
li.print_list()
print(li.get(0))