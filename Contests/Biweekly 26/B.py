def simplifiedFractions(n: int):
    if n == 1:
        return []
    
    ans = []
    for i in range(1, n):
        for j in range(i+1, n+1):
            # if coprime(i, j):  
            if gcd(i, j) == 1:
                ans.append(f'{i}/{j}')
    return ans

def coprime(a, b):
    # O(min(a, b))
    mi = min(a, b)
        
    for i in range(2, mi+1):
        if a%i ==0 and b%i==0:
            return False
    return True

# Euclidean algorithm
def gcd(a, b):
    # O(log (ab)) - much faster than my coprime algorithm which i used in competition
    if b==0:
        return a
    return gcd(b, a%b)

# print(simplifiedFractions(6))