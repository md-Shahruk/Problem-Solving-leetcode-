
## Time: O(nlogn)  for sorting
def solve(nums):
    nums.sort()
    for i in range(0, len(nums) - 1, 2):
        if nums[i]!=nums[i+1]:
            return nums[i]
    return nums[-1]

def solve2(nums):
    res = 0
    for i in range(len(nums)):
        res ^= i # when num appear 2 times if three times ones = (ones ^ num) & ~twos
    return res 
    
## math 2*sum_of_unique -  actual sum
nums = [4,1,2,1,2]
print(solve2(nums))