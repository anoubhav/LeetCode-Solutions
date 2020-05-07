from collections import Counter

J = "aA"
S = "aAAbbbb"

def my_soln(J, S):
    ans = 0
    d = Counter(S)
    for jewel in J:
        try:
            ans += d[jewel]
        except:
            continue
    return(ans)

# From discussion page.
def numJewelsInStones(J, S):  # O(J*S)
    return sum(map(J.count, S))
    # return sum(map(S.count, C))

print(my_soln(J, S))
print(numJewelsInStones(J, S))