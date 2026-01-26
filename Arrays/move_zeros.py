
## Time: O(n) and space O(n)
def solve(nums):
    n = len(nums)
    c = 0
    new_num = []
    for i in range(n):
        if nums[i] != 0:
            new_num.append(nums[i])
            
    while len(new_num) < n:
        new_num.append(0)
           
    return new_num


## Time: O(n) 
def solve2(nums):
    l, r = 0, 0
    while r < len(nums):
        if nums[r] != 0:
            nums[l] = nums[r]
            l += 1
            r += 1
        else:
            r += 1
    while l < len(nums):
        nums[l] = 0
        l += 1
    return nums 
        
    
nums = [0] 
print(solve2(nums))