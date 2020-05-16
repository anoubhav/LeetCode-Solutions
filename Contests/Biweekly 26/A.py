# https://leetcode.com/problems/consecutive-characters/

def maxPower(s: str) -> int:
    ans = 1
    prev = s[0]
    temp = 1
    for char in s[1:]:
        if char == prev:
            temp += 1
        else:
            temp = 1
            prev = char
        
        ans = max(ans, temp)
        
    return ans

print(maxPower('leetcode'))