# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3291/

import itertools
def str_remove(S):
    # Time complexity: linear
    # Space complexity: linear

    finals = ''
    for char in S:
        if char!='#': finals += char
        else: 
            if len(finals)>0:
                finals = finals[:-1]
    return finals

def F(S):
    # O(N) time and O(1) space
    skip = 0
    for char in reversed(S):
        if char == '#':
            skip +=1
        elif skip:
            skip -=1
        else:
            yield char

def backspaceCompare(S, T):
    # return str_remove(S) == str_remove(T)

    return all(x==y for x, y in itertools.zip_longest(F(S), F(T)))

print(backspaceCompare('ab#c', 'ad#c'))

