# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3293/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def diameterOfBinaryTree(root):
    height = 1

    def height(node):
        if node is None:
            return 0
        l_height = height(node.left)
        r_height = height(node.right)
        height = max(height,l_height+r_height+1)
        return max(l_height,r_height) + 1

    height(root)
    return height-1

        
        