from collections import Counter
# My solution
def my_soln(ransomNote, magazine): # O(m+n)
    d = Counter(magazine) # O(m)

    for char in ransomNote: # O(n)
        if char not in d:
            return False
        elif d[char] == 0:
            return False
        else:
            d[char] -= 1
    return True

# Discussion page
def canConstruct(ransomNote, magazine):
    return Counter(ransomNote) - Counter(magazine) == {}

print(my_soln('aa', 'aab'))
print(canConstruct('aa', 'aab'))