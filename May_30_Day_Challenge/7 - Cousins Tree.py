# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS solution; faster than 97% of the users
def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

    x_parent, x_depth, y_parent, y_depth = None, None, None, None
    
    def dfs(node, depth, parent):
        
        # use and modify the variables outside the inner nested scope
        nonlocal x, y, x_parent, x_depth, y_parent, y_depth
        
        if node == None:
            return
        
        if x_parent and y_parent:
            return
        
        elif node.val == x:
            x_parent = parent
            x_depth =  depth
        
        elif node.val == y:
            y_parent = parent
            y_depth = depth
        
        dfs(node.left, depth + 1, node)
        dfs(node.right, depth + 1, node)
    
    dfs(root, 0, None)
    
    if x_depth == y_depth and x_parent.val!=y_parent.val:
        return True
    else:
        return False

# BFS solution
def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    from collections import deque

    soln = {}
    d = deque([(root, 0, 0)])
    # root, depth, parent
    curr, depth, parent = None, None, None
    while d:
        curr, depth, parent = d.popleft()

        if len(soln) == 2: break
        if curr.val == x or curr.val == y:
            soln[curr.val] = [depth, parent]

        if curr.left:
            d.append((curr.left, depth + 1, curr))

        if curr.right:
            d.append((curr.right, depth + 1, curr))

    return (soln[x][0] == soln[y][0]) & (soln[x][1]!=soln[y][1])
