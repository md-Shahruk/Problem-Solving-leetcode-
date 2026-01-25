"""
Time: O(n) where n is len of nums
Space: O(1) use only constant extra space
"""

def brute_force_solve(nums, val):
    if not nums:
        return 0
    
    res = 0
    l = len(nums)
    for x in range(l):
        if nums[x] != val:
                nums[res] = nums[x]
                res += 1
    return res 
    
nums = [3,2,2,3]
val = 3
print(brute_force_solve(nums, val))