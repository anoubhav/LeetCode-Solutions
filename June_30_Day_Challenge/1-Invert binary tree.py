class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Using graph traversal: BFS + Queue
def invertTreeBFS(root: TreeNode) -> TreeNode:
    if not root:
        return root

    from collections import deque
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        node.left, node.right = node.right, node.left
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
        
    return root

# Using recursion
def invertTreeRecursion(self, root: TreeNode) -> TreeNode:
    
    def invert_tree(node):
        if not node:
            return
        right = invert_tree(node.right)
        left = invert_tree(node.left)
        node.right = left
        node.left = right
        return node
    
    return invert_tree(root)

# discussion page
def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
        return root

## Time and space complexity:

# BFS solution
# Since each node in the tree is visited / added to the queue only once, the time complexity is O(n), where n is the number of nodes in the tree.

# Space complexity is O(n), since in the worst case, the queue will contain all nodes in one level of the binary tree. For a full binary tree, the leaf level has ceil(n/2) = O(n) leaves.

# Recursive solution
# Since each node in the tree is visited only once, the time complexity is O(n), where n is the number of nodes in the tree. We cannot do better than that, since at the very least we have to visit each node to invert it.

# Because of recursion, O(h) function calls will be placed on the stack in the worst case, where h is the height of the tree. Because h∈O(n), the space complexity is O(n).