class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(root1: TreeNode, root2: TreeNode) -> bool:
    def dfs(root):
        stack = []
        stack.append(root)
        lvs = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                lvs.append(node.val)
                
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return lvs
    
    lvs1, lvs2 = dfs(root1), dfs(root2)
    
    return lvs1 == lvs2

import itertools
def leafSimilar_yield(root1: TreeNode, root2: TreeNode) -> bool:
    def dfs(node):
            if not node: return
            if not node.left and not node.right: yield node.val
            for i in dfs(node.left): yield i
            for i in dfs(node.right): yield i
            
    return all(a == b for a, b in itertools.zip_longest(dfs(root1), dfs(root2)))