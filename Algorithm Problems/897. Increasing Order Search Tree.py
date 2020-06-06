class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def newTreeincreasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return []
        
        def inorder(root):
            if not root: return []
            return inorder(root.left)+ [root.val] + inorder(root.right)
        lst = inorder(root)
        
        head = parent = TreeNode(lst[0])
        for i in lst[1:]:
            parent.right = TreeNode(i)
            parent = parent.right
        
        return head
    
    def sameTreeincreasingBST(self, root: TreeNode) -> TreeNode:
        def increasingBST(root, tail = None):
            if not root: return tail
            res = increasingBST(root.left, root)
            root.left = None
            root.right = increasingBST(root.right, tail)
            return res

        return increasingBST(root, None)
