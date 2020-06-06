class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# DFS + Stack. O(N) time complexity, where N is the number of nodes. O(N) space complexity.
def maxDepth_iteration(root: 'Node') -> int:
    if not root:
        return 0
    stack = []
    stack.append((root, 1))
    maxdepth = 0
    while stack:
        node, depth = stack.pop()
        if depth>maxdepth: maxdepth = depth
            
        for child in node.children:
            stack.append((child, depth + 1))
    return maxdepth

# DFS + recursion. O(N) time complexity, O(H) space complexity, where H is the height of tree.
def maxDepth_recursion(root: 'Node') -> int:
    if not root:return 0
    maxdepth = 0
    for child in root.children:
        maxdepth = max(maxdepth, maxDepth_recursion(child))
    return maxdepth + 1