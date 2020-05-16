# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS recursively    
def hasPathSum(root: TreeNode, sum: int) -> bool:
    curr = 0
    flag = 0
    if not root: return False

    def dfs(node, curr):
        nonlocal flag
        curr += node.val

        # if its a leaf node check if path sum equals
        if node.left == None and node.right == None:
            if curr == sum: flag = 1
            return

        if node.left: dfs(node.left, curr)
        if node.right: dfs(node.right, curr)      

    dfs(root, curr)
    if flag: return True
    return False

# Discussion page : DFS recursive
def disc_hasPathSum(root, sum):
    if not root:
        return False

    if not root.left and not root.right and root.val == sum:
        return True
    
    sum -= root.val

    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)
            

def dfs_stack(root, sum):
    if not root: return False

    stack = [(root, root.val)]

    while stack:
        node, currsum = stack.pop()

        if not node.left and not node.rigth and currsum = sum:
            return True

        if node.left: stack.append((node.left, currsum + node.left.val))   
        if node.right: stack.append((node.right, currsum + node.right.val)) 

    return False


def bfs_queue(root, sum):
    from collections import deque
    if not root: return False
    
    d = deque([(root, root.val)])
    while d:
        node, currsum = d.popleft()

        if node.left == None and node.right == None and currsum == sum:
            return True
        
        if node.left: d.append((node.left, currsum + node.left.val))
        if node.right: d.append((node.right, currsum + node.right.val))
    return False
        