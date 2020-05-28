## Concepts: DFS, graph coloring, bipartite graph (bigraph), even and odd edge cycles in a graph, connected components.
# A bigraph can only have even edge cycles. If it has odd length cycles, vertices in the same set will no longer be disjoint.

N = 10
dislikes = [[4,7],[4,8],[2,8],[8,9],[1,6],[5,8],[1,2],[6,7],[3,10],[8,10],[1,5],[7,10],[1,10],[3,5],[3,6],[1,4],[3,9],[2,3],[1,9],[7,9],[2,7],[6,8],[5,7],[3,4]]

# N  = 5
# dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]



from collections import defaultdict, deque
def iterative_set(N, dislikes):
    # from discussion page. The 'remaining' list idea is what I was missing when I first tried sets.
    if len(dislikes)<=1:
        return True
    
    while dislikes:
        g1 = set()
        g2 = set()
        g1.add(dislikes[0][0])
        g2.add(dislikes[0][1])
        rem = []
        for i in range(1, len(dislikes)):
            a, b = dislikes[i][0], dislikes[i][1]
            if a in g1 and b in g1:
                return False
            elif a in g2 and b in g2:
                return False
            elif a in g1 and b in g2:
                continue
            elif a in g2 and b in g1:
                continue
            elif a in g1:
                g2.add(b)
            elif b in g1:
                g2.add(a)
            elif a in g2:
                g1.add(b)
            elif b in g2:
                g1.add(a)
            else:
                rem.append(dislikes[i])
        
        dislikes = rem
    
    return True

def twocolor_bfs(N, dislikes):

    def bfs(node):
        q = deque()
        q.append(node)

        while q:
            curr = q.popleft()
            for nbr in g[curr]:
                if colors[nbr] == 0: 
                    colors[nbr] = -colors[curr]
                    q.append(nbr)
                else:
                    if colors[nbr] == colors[curr]:
                        return False
        return True
        
    colors = defaultdict(int)
    g = defaultdict(list)

    for a, b in dislikes:
        g[a].append(b)
        g[b].append(a)
    
    for i in range(N):
        if colors[i] == 0:
            colors[i] = 1
            if not bfs(i):
                return False
        else:
            continue

    return True

def twocolor_dfs(N, dislikes):
    # mysoln_3. O(V+E)
    g = defaultdict(list)

    for edge in dislikes:
        a, b = edge
        g[a].append(b)
        g[b].append(a)
    
    visited = [0]*(N+1)
    colors = [0]*(N+1)

    ans = True
    def dfs(node, parent):
        nonlocal ans
        visited[node] = 1

        if parent: colors[node] = -colors[parent]

        for nbrs in g[node]:
            if nbrs != parent:
                if not visited[nbrs]:
                    dfs(nbrs, node)
                else:
                    # if visited already
                    if colors[node] == colors[nbrs]:
                        ans = False

    for i in range(1, N+1):
        # if already there is a adjacent same color violation in a connected component break
        if ans is False:
            break

        # if already visited then move to next node.
        if visited[i]:
            continue

        else:
            # perform dfs if unvisited. (new connected component)
            colors[i] = 1
            dfs(i, None)

    return ans

def recurive_set_tle(N, dislikes):
    #TLE; but correct final answer. Uses recursion.
    def recurse(i, g1, g2):
        if i == len(dislikes):
            return True
        
        a, b = dislikes[i]
        # print(i, g1, g2)
        if (a in g1 and b in g1) or (a in g2 and b in g2):
            return False

        if a in g1:
            g2.add(b)
            ans = recurse(i+1, g1.copy(), g2.copy())
        elif a in g2:
            g1.add(b)
            ans = recurse(i+1, g1.copy(), g2.copy())
        elif b in g1:
            g2.add(a)
            ans = recurse(i+1, g1.copy(), g2.copy())
        elif b in g2:
            g1.add(a)
            ans = recurse(i+1, g1.copy(), g2.copy())
        else:
            g1.add(a)
            g2.add(b)
            ans1 = recurse(i+1, g1.copy(), g2.copy())

            g1 -= {a}
            g2 -= {b}
            g1.add(b)
            g2.add(a)
            ans2 = recurse(i+1, g1.copy(), g2.copy())

            ans = ans1 | ans2
        
        return ans

    return recurse(0, set(), set())

print(twocolor_bfs(N, dislikes))
print(recurive_set_tle(N, dislikes))
print(twocolor_dfs(N, dislikes))


