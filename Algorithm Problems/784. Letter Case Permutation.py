import itertools
def itertools_letterCasePermutation(S):
    L = [[i.upper(), i.lower()] if i.isalpha() else i for i in S]
    return [''.join(i) for i in itertools.product(*L)]


# BFS + queue
from collections import deque
def bfs_letterCasePermutation(S):
    q = deque()
    q.append('')
    for char in S:
        if char.isalpha():
            size = len(q)
            while size:
                string = q.popleft()
                q.append(string + char.upper())
                q.append(string + char.lower())
                size -= 1
        else:
            for i in range(len(q)):
                q[i] += char
    return q

def dfs_backtrack_letterCasePermutation(S):
    def backtrack(sub="", i=0):
        if len(sub) == len(S):
            res.append(sub)
        else:
            if S[i].isalpha():
                backtrack(sub + S[i].swapcase(), i + 1)
            backtrack(sub + S[i], i + 1) 
    res = []
    backtrack()
    return res

def iteration_letterCasePermutation(S):
    res = ['']
    for ch in S:
        if ch.isalpha():
            res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
        else:
            res = [i+ch for i in res]
    return res

    ## Soln 2
    # res = [S]
    # for i, c in enumerate(S):
    #     if c.isalpha():
    #         res.extend([s[:i] + s[i].swapcase() + s[i+1:] for s in res])
    # return res

S = "a1b2"
print(*itertools_letterCasePermutation(S))
print(*bfs_letterCasePermutation(S))
