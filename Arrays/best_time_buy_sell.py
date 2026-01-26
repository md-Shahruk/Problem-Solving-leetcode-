
## brute force solution
## Time: O(n^2) 
def solve(prices):
    l = len(prices)
    max_s = 0
    for i in range(l):
        for j in range(i+1,l):
            if prices[j] > prices[i]:
                c = prices[j] - prices[i]
                max_s = max(c, max_s)
    return max_s

## Time: O(n)
def solve2(prices):
    l, r = 0, 1
    max_s = 0
    while r < len(prices):
        if prices[r] > prices[l]:
            c = prices[r] - prices[l]
            max_s = max(max_s, c)
            r += 1
        else:
            l = r 
            r += 1
    return max_s
               

prices = [7,10,5,21,6,4]
print(solve2(prices))