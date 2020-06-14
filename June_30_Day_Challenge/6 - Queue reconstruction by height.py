from collections import defaultdict
def lowTohigh_reconstructQueue(people):

    # O(N^2) time complexity, O(N) space complexity
    n = len(people)
    g = defaultdict(set)
    for h, k in people:
        g[h].add(k)
    
    heights = sorted(g.keys())
    
    ans = [0]*n
    for h in heights:
        inds = g[h]
        count = 0
        for i in range(n):
            if ans[i] == 0:
                if count in inds:
                    ans[i] = [h, count]
                    inds.remove(count)
                count += 1
                    
            if len(inds) == 0:
                break
    return ans

def highTolow_reconstructQueue(people):
    # O(N^2) time complexity
    people.sort(key = lambda x: (-x[0], x[1]))
    queue = []
    for p in people:
        # insertion takes O(N)
        queue.insert(p[1], p)
    return queue