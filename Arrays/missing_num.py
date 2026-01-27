
## Time: O(nlogn) for sorting
def solve(nums):
    l = len(nums)
    nums.sort()
    for i in range(0, l):
        if nums[i] != i:
            return i 
    return l  

## Time: O(n) using math formula n*(n+1) // 2
def solve2(nums):
    l = len(nums)
    e_s = l*(l+1) // 2
    s = sum(nums)
    return e_s - s 
nums = [0,1]
print(solve2(nums))