
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 

def linkedlist(values, pos):
    if not values:
        return None
    nodes = [ListNode(val) for val in values] 
    for i in range(len(values) - 1):
        nodes[i].next = nodes[i+1]
    if pos > -1 and pos < len(values):
        nodes[-1].next = nodes[pos]
    return nodes[0]

# Time: O(n) Space: O(1) for slow , fast constant
def hasCycle(nodes):
    s= f = nodes
    while f and f.next:
        s = s.next
        f = f.next.next
        if s == f:
            return True
    return False


values = [1,2,3,4]
pos = 1 
head = linkedlist(values, pos)

print(hasCycle(head))