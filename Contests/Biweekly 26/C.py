class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS + stack solution (used in competition)
def goodNodes(root: TreeNode) -> int:
    # O(n) time complexity  
    stack = [(root, root.val, root.val)]
    
    ans = 1
    while stack:
        node, value, msf = stack.pop()
        
        if node.left == None and node.right == None:
            continue
        
        if node.left: 
            temp = node.left.val if node.left.val > msf else msf
            if temp == node.left.val: ans +=1
            stack.append((node.left, node.left.val, temp))

        if node.right: 
            temp = node.right.val if node.right.val > msf else msf
            if temp == node.right.val: ans +=1
            stack.append((node.right, node.right.val, temp))
            
    return ans


## DFS + Recursion
# 1. Update the maximum value found while recurse down to the paths from root to leaves;
# 2. If node value >= current maximum, count it in.
# 3. return the total number after the completion of all recursions.

def goodNodes_recursion(self, root: TreeNode) -> int:
    
    def count(node: TreeNode, v: int) -> int:
        if node is None:
            return 0
        mx = max(node.val, v)
        return (node.val >= v) + count(node.left, mx) + count(node.right, mx)
    
    return count(root, root.val)

