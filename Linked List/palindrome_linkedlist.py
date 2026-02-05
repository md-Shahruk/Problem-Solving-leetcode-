class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linkedList(values):
    if not values:
        return None 
    nodes = [Node(val)  for val in values]
    for i in range(len(values) -1):
        nodes[i].next = nodes[i+1]
    return nodes[0]
"""
we can see here for below reverse list:
Time: O(n) and Space O(n) for copy list 
"""
def reverse_list(head):
    cur = head
    prev = None
    trac = head
    while cur:
        n = cur.next
        cur.next = prev
        prev = cur
        cur = n 
    return prev

""" 
Another approach we will apply here:
- find the half or linkedlist using slow fast
- reverse only second half
- then make compare between head and reverse head
Time: O(n) Space: O(1)
"""
def reverse_list_new(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    prev = None 
    cur = slow
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    
    l = head
    r = prev
    while r:
        if l.val != r.val:
            return False
        l = l.next
        r = r.next
    return True
    
def copy_list(head):
    if not head:
        return None 
    new_head = Node(head.val)
    orginal = head.next
    current = new_head
    
    while orginal:
        new_node = Node(orginal.val)
        current.next = new_node
        current = current.next
        orginal = orginal.next
    return new_head 

def check_palindrome(orginal, reverse):
    cur1= orginal
    cur2 = reverse
    
    while cur1 and cur2:
        if cur1.val != cur2.val:
            return False
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1 is None and cur2 is None

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" " if curr.next else "")
        curr = curr.next
    print()


values = [1,2,2,1]
head = linkedList(values)
copy = copy_list(head)
rev = reverse_list(head)
pal = check_palindrome(copy, rev)
rev_new = reverse_list_new(head)

print(rev_new)