# 1651 / 8571	anoubhav 	7	0:05:31:	 0:02:47	 0:05:31     NS       NS
# Could solve only 2 out of 4. But, 2 were solved very fast.
# problem A is trivial

def mysoln_finalPrices(prices):
    # O(N^2) time complexity. nested for loops. O(1) space complexity. Naive.
    n = len(prices)
    for i in range(n):
        for j in range(i+1, n):
            if prices[j] <= prices[i]:
                prices[i] -= prices[j]
                break
    return prices

def increasing_stack(prices):
    # O(N) time complexity. O(N) space. 
    # Concept: Monotone stack: use it to find: 
    # 1) next greater element: mantain decreasing stack, traverse from left to right
    # 2) prev greater element: mantaint decreasing stack, traverse from right to left
    # 3) next smaller element: mantain increasing stack, traverse from left to right
    # 4) prev smaller element: mantain increasing stack, traverse from right to left

    stack = []
    for i in range(len(prices)):
        while stack and prices[i] <= prices[stack[-1]]:
            prices[stack.pop()] -= prices[i]
        stack.append(i)
    return prices
            



