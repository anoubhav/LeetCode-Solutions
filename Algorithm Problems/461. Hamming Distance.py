def hammingDistance(x: int, y: int) -> int:
    ## O(log max(x, y)): soln 1
    # x, y = bin(x)[2:][::-1], bin(y)[2:][::-1]
    # ans = 0
    # if len(x) < len(y):
    #     x, y = y, x

    # for i in range(len(y)):
    #     if x[i]!=y[i]: ans+=1

    # for i in range(len(y), len(x)):
    #     if x[i] == '1':
    #         ans += 1
    # return ans

    ## soln 2
    # ans = 0
    # while x>0 or y>0:
    #     # ans += (x & 1 != y & 1)
    #     x >>= 1
    #     y >>= 1
    # return ans

    ## soln 3
    # return bin(x^y).count('1')

    ## soln 4
    # ans, n = 0, x^y
    # while n>0:
    #     ans += 1
    #     n &= n-1   #  Brian Kernighan's algorithm for counting set bits.
    # return ans
        