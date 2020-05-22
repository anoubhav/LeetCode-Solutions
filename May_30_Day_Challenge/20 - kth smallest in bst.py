# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursion + DFS ( my first submission )
def my_soln(root, k):
    # Intuition: inorder traversal of BST is an array sorted in the ascending order. I am decrementing the k count
    # everytime the node is visited. On reaching the kth smallest, I am setting the val (answer). However, we cannot just exit the inner recursion. So the traversal has to complete before I return the answer.

    # O(N) time complexity, In-order traversal of all nodes. # O(1) space.
    val = None

    def inorder_traversal(node):
        nonlocal k, val
        if node:
            # left node
            ret = inorder_traversal(node.left)
            
            if ret!=None:
                k-=1
                if k == 0:
                    val = node.left.val
            
            # parent node
            k-=1
            if k == 0: 
                val = node.val
            
            # right node
            ret = inorder_traversal(node.right)
            
            if ret!=None:
                k-=1
                if k == 0:
                    val = node.right.val
    
    inorder_traversal(root)
    
    return val

# Recursion + DFS
def soln_two(root, k):
    # Same intuition as above. Time complexity: O(N), space complexity: O(N)
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []
    
    return inorder(root)[k-1]

# Stack + DFS (iteration)
def soln_three(root, k):
    # Using iteration we can stop on reaching the kth smallest element instead of traversing the entire tree.

    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left

        # if k>N
        if stack == []: return -1

        root = stack.pop()
        k-=1
        if k == 0: return root
        root = root.right

    # Time complexity :{O}(H + k)O(H+k), where HH is a tree height. This complexity is defined by the stack, which contains at least H + kH+k elements, since before starting to pop out one has to go down to a leaf. This results in O(logN+k) for the balanced tree and O(N+k) for completely unbalanced tree with all the nodes in the left subtree.

    # Space complexity : O(H+k), the same as for time complexity, O(N+k) in the worst case, and O(logN+k) in the average case.

# Priority Queue using Heaps
def soln_four(root, k):
    import heapq
    
    nodes = []
    
    # O(N) ; You can perform any traversal. You just want the list of nodes of the tree
    def preorder(node):
        if not node: return
        nodes.append(node.val)
        preorder(node.left)
        preorder(node.right)
    
    preorder(root) # fills up the list: nodes

    # return nodes[k-1] ; Only gives correct solution if performing inorder traversal

    n = len(nodes)
    
    # O(N) heap construction. O(min (k, N-k) log N) polling/popping.
    if k > n//2:
        # e.g., n = 100, and k = 90, this is 90th smallest element. You can instead find the (n-k+1)th, 11th largest element. If k>n//2, create a max heap instaed.

        # Max heap by negation of numbers
        nodes = [-i for i in nodes]
        heapq.heapify(nodes)
        rem = n - k

        while rem >= 0:
            elem = heapq.heappop(nodes)
            rem -= 1
        elem = -1*elem
        
    else:
        heapq.heapify(nodes)
    
        # O(k log N)
        while k>0:
            elem = heapq.heappop(nodes)
            k -= 1

    return elem

# Recursion + DFS (using 'yield' and generators to stop it at kth element, instead of full traversal)
def soln_five(root, k):
    def traverse(node):
        if node:
            yield from traverse(node.left)
            yield node
            yield from traverse(node.right)
        
    k -= 1 # enumerate starts from 0 indexing.
    
    for i, node in enumerate(traverse(root)):
        if i == k:
            return node.val