# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/

def isHappy(n):
    prev = {}

    while n!=1:
        sqsum = 0
        while n!=0:
            sqsum += (n%10)**2
            n = n//10
        n = sqsum

        if n not in prev:
            prev[n] = 0
        else:
            return False
    return True

print(isHappy(2))