favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
# Output: [0,1,2, 3] 

# index - list : (key, value)
d = dict()
for ind, lst in enumerate(favoriteCompanies):
    d[ind] = set(lst)

ans = [] # stores the indexes, i.e., the keys
for k1, v1 in d.items():
    flag = 1
    for k2, v2 in d.items():
        if k2!=k1:
            if v1.issubset(v2):
                flag = 0
                break

    if flag: ans.append(k1)

print(ans)
    

    

