def dfs_top_sort(numCourses, prerequisites):
    n, pr = numCourses, prerequisites.copy()
    # Is it a DAG? Does it contain cycles
    def hasCycle(g, node):
        if visited[node] == 1:
            return True
        elif visited[node] == 2:
            return False
        else:
            visited[node] = 1
            for nbr in g[node]:
                if hasCycle(g, nbr):
                    return True

            visited[node] = 2
            stk.append(node)
            return False
        
    from collections import defaultdict
    g = defaultdict(list)
    stk = []
    for a, b in pr:
        g[b].append(a)
    visited = [0]*n # 0 - unvisited ; 1 - in call stack ; 2 - explored
    
    for i in range(n):
        if visited[i] == 0:
            if hasCycle(g, i):
                return False
    return True