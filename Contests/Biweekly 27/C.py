
# DFS (using recursion) for each starting node (max 100), full traversal each time.
def my_soln(n, prerequisites, queries):
    # Time complexity: O(N*(N+E)) ; Space complexity: O(N*N).

    # When I got TLE, I performed DFS for each query. Time complexity: O(Q*(N+E)). Space complexity: O(N*N) for graph
    from collections import defaultdict
    prereq = defaultdict(set)

    for a, b in prerequisites:
        prereq[a].add(b)


    def dfs(start, target):
        nonlocal flag
        # global flag

        visited[start] = 1

        if start == target:
            flag = True

        for nbr in prereq[start]:
            if not visited[nbr]:
                dfs(nbr, target)
        return visited

    ans = []
    d = dict() # store all the nodes you can visit from starting node i.
    for a, b in queries:
        # if traversal has already been performed for a, query in O(1)
        if a in d:
            if b in d[a]:
                ans.append(True)
            else:
                ans.append(False)
        else:
            # perform traversal and store the possible visited nodes in dictionary.
            flag = False
            visited = [0]*(n+1)
            visited = dfs(a, b)
            d[a] = set(i for i, num in enumerate(visited) if num==1)
            ans.append(flag)

    return ans



# BFS (using queue) for each query (max 10^4), break if target found.
def discpage_bfs(n, prerequisites, queries):
    # Time complexity: O(Q*(N+E)). This works, and DFS does not because we can break early when target is found instead of performing full traversal.
    graph = [[] for _ in range(n)]
    for u, v in prerequisites:
        # need u to do v
        graph[u].append(v)
    
    ans = []
    for qs, qt in queries:
        stack = [qs]
        seen = {qs}
        while stack:
            node = stack.pop()
            if node == qt:
                ans.append(True)
                break
            for nei in graph[node]:
                if nei not in seen:
                    stack.append(nei)
                    seen.add(nei)
        else:
            ans.append(False)
    return ans
                

def floyd_warshall_algorithm(n, prerequisites, queries):
    # Time complexity: O(N^3). Space complexity: O(N^2)
    
    connected = [[False]*n for i in range(n)]
    for a, b in prerequisites:
        connected[a][b] = True

    for k in range(n):
        for j in range(n):
            for i in range(n):
                connected[i][j] = connected[i][j] or (connected[i][k] and connected[k][j])

    return [connected[i][j] for i, j in queries]