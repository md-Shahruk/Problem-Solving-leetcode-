
"""
Time: O(n) where n is len of nums
Space: O(1) use only constant extra space
"""
def brute_force_solve(nums):
        res = 1
        l = len(nums)
        for x in range(1, l):
            if nums[x-1] != nums[x]:
                 nums[res] = nums[x]
                 res += 1
        return res 
        
    
   

nums = [3,3,3]
print( brute_force_solve(nums))