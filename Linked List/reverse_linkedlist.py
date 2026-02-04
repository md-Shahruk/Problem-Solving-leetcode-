

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
class LinkedList:
    def __init__(self):
        self.dummyhead = ListNode()
        self.size = 0
    
    def addLast(self,value):
        new_node = ListNode(value)
        current =  self.dummyhead
        while current.next:
            current =  current.next
        current.next = new_node
        self.size +=1 
    
    # Time: O(n) and Space: O(n)
    # def reverse_list(self):
    #     cur = self.dummyhead.next
    #     li = []
    #     while cur:
    #         li.append(cur)
    #         cur = cur.next
    #     n_node = li.pop()
    #     cur = n_node
    #     while li:
    #         cur.next = li.pop()
    #         cur = cur.next
    #     cur.next = None
    #     self.dummyhead.next = n_node
    #     return n_node 
            
    def reverse_list(self):
        cur = self.dummyhead.next
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
    
    def print_r_list(self, node=None):
        if node is None:
            return None
        else:
            cur =  node 
        while cur:
            print(cur.val , end=" " if cur.next else "")
            cur = cur.next
        print()
            
        
    
    
    
    
    
    # def print_list(self):
    #     current =  self.dummyhead.next
    #     while current:
    #         print(current.val, end="-")
    #         current = current.next 
    

li = LinkedList()
li.addLast(1)
li.addLast(2)
li.addLast(3)
li.addLast(4)
li.addLast(5)


new = li.reverse_list()
li.print_r_list(new)
