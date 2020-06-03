def deleteNode(node):

    curr = node
    while curr.next:
        curr.val = curr.next.val
        prev = curr
        curr = curr.next
    
    prev.next = None
    del curr

# way better. Replace current node (to be deleted) value with next node. And skip next node to avoid repitition.
def discpage(node):
    node.val = node.next.val
    node.next = node.next.next
