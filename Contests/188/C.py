# Unsolved

# Src1: https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/discuss/623673/Concise-explanation-with-a-Picture-for-Visualization

def minTime(n, edges, hasApple):
    # O(n) time complexity ; visit each node once; O(|E|) space complexity
    adj = [[] for _ in range(n)]

    # create an adjacency list for the graph
    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)
    
    visited = set()
    def dfs(node):
        # if visited don't include in time calculation
        if node in visited:
            return 0
        visited.add(node)

        # seconds
        secs = 0
        for child in adj[node]:
            # Add the time is takes to traverse each child in subtree of node which contains an apple before returning back here.
            secs += dfs(child)
        
        # while going back up the tree if the subtree below the current node had an apple, increment the # of seconds
        # by 2. Going down this node + going back up this node.
        if secs>0:
            return secs + 2

        else:
            # if leaf node has apple return 2 else 0
            return 2 if hasApple[node] else 0

    return max(dfs(0) - 2, 0)

print(minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False]))