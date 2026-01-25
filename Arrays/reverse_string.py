

def solve(s):
    l = len(s)
    res = ['']*l ## Space: O(n) for
    for i in range(l): ## Time: O(n)
        res[i] = s[(l-1) - i]
    return res 
    
def solve2(s):
    l = len(s)
    """
    Space: O(1) no extra memory
    Time: O(n)
    """
    for i in range(l//2):
        s[i], s[(l-1) - i] = s[(l-1) - i], s[i]
    return s 
s = ["h","e","l","l","o"]
print(solve2(s))