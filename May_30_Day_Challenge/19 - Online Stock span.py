class LinearScan_StockSpanner:
    # TLE
    def __init__(self):
        self.prices = []
        
    def next(self, price: int) -> int:
        self.prices.append(price)
        
        ans = 0
        for p in self.prices[::-1]:
            if p<=price:
                ans +=1
            else:
                break
        return ans

class mysoln_StockSpanner:
    # Accepted. However, it is not memory efficient. Most elements of prevspan are not required after a couple runs. To find the answer instead of linearly scanning, we hop from end to beginning based on precomputed spans.
    def __init__(self):
        self.prices = []
        self.prevspan = []
        

    def next(self, price: int) -> int:
        self.prices.append(price)
        ans = 1
        ind = len(self.prices)-2
        while ind>=0 and self.prices[ind]<=price:
            t = self.prevspan[ind]  
            ans += t
            ind -= t
            
        self.prevspan.append(ans)
        return ans

class stack_StockSpanner:
    def __init__(self):
        self.stack = []
    
    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0]<=price:
            ans += self.stack.pop()[1]

        self.stack.append((price, ans))
        return ans