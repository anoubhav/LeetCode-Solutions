def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] - prices[i-1] > 0:
            profit += prices[i] - prices[i-1]
    return profit

def maxProfitDP(prices):
    nothing, own = 0, -10**9 # the max profit inititally holding no stock and holding a stock respectively.
    for p in prices:
        new_nothing = max(nothing, own + p)
        new_own     = max(own, nothing - p)
        nothing, own = new_nothing, new_own
    return nothing

print(maxProfit([7,1,5,3,6,4]))
print(maxProfitDP([7,1,5,3,6,4]))