import sys
sys.setrecursionlimit(2*10**5)
def dfs_top_sort(n, pr):
    from collections import defaultdict
    # If not a DAG, impossible, If a DAG, return top sort.
    def topsort(g, node):
        if visited[node] == 1:
            return True
        if visited[node] == 2:
            return False
        
        visited[node] = 1
        for nbr in g[node]:
            if topsort(g, nbr):
                return True
        visited[node] = 2
        stk.append(node)
        return False
    
    g = defaultdict(list)
    for a, b in pr:
        g[b].append(a)
    
    visited = [0]*n # 0 - unvisited, 1 - on call stack, 2 - explored
    stk = [] # topsort
    
    for i in range(n):
        if visited[i] == 0:
            if topsort(g, i): # if it contains cycle
                return []
    
    return stk[::-1]

prerequisites = [[1,0],[2,0],[3,1],[3,2]]
numCourses = 4

print(dfs_top_sort(numCourses, prerequisites))
            
            
        
        
        
        
        