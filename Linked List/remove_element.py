
class Node:
    def __init__(self,val=0, next=None):
        self.val = val 
        self.next = next 
def linkedList(values):
    head = [Node(val) for val in values]
    for i in range(len(values) - 1):
        head[i].next = head[i+1]
    return head[0]

def remove_element(head, val):
    while head and head.val == val:
        head = head.next
    cur = head
    new_head = cur 
    while cur and cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return new_head
    
       

def print_list(head):
    cur = head 
    while cur:
        print(cur.val, end=" " if cur.next else "")
        cur = cur.next
    print()

values = [1,2,3,6,4,5,6]
he = linkedList(values)
val = 6
re = remove_element(he,val)
print_list(re)