
 ## Time: O(n) 
def solve(nums):
    max_o = 0
    c = 0
    l = len(nums)
    for i in range(l):
        if nums[i] == 1:
            c += 1
            max_o = max(max_o, c)
        else:
            c = 0
    return max_o

def sliding(nums):
    max_o = 0
    l, r = 0, 0
    for r in range(len(nums)):
        if nums[r] == 0:
            l = r + 1
        else:
            c = r - l + 1
            max_o = max(c, max_o)
    return max_o
nums = [1,0,1,1,0,1,1,0,0,0,0,0,1,0,1,1,1,1,0]
print(sliding(nums))