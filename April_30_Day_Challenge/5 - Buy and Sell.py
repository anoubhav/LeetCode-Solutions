# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3287/

def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i]>prices[i-1]:
            profit += (prices[i] - prices[i-1])
    return profit

print(maxProfit([7,1,5,3,6,4]))