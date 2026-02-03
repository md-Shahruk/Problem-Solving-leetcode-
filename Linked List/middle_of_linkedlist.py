
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
        
    def middleofthelist(self):
        if self.size == 0:
             return None 
        index = self.size//2
        current = self.dummyhead.next
        for i in range(index):
            current = current.next
        return current.val
        """
        slow , fast two pointer technique
        slow: takes 1 step at a time
        fast: takes 2 step at a time 
        when the fast reach the end , the slow at  the middle
        
        """
    def slow_fast(self):
        if not self.dummyhead.next:
            return None 
        slow = self.dummyhead.next
        fast = self.dummyhead.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val 
    
    
    def print_list(self):
        current =  self.dummyhead.next
        while current:
            print(current.val, end="-")
            current = current.next

li = LinkedList()
li.addLast(1)
li.addLast(2)
li.addLast(3)
li.addLast(4)
li.addLast(5)


#print(li.middleofthelist())
print(li.slow_fast())
