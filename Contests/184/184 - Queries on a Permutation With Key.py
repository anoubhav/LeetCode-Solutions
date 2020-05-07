def processQueries(queries, m):
    P = list(range(1, m+1))
    ans = []
    for query in queries:
        pos = -1
        for i in range(m): 
            if P[i] == query:
                pos = i
        
        temp = P[pos]
        ans.append(pos)
        del P[pos]
        P = [temp] + P
        
    return ans

print(processQueries(queries = [7,5,5,8,3], m = 8))