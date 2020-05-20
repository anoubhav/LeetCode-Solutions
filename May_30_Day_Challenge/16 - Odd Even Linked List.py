# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # O(N) we visit each node once. O(1) in place solution.
        
        if head == None:
            return head
        
        curr = head
        evenhead = curr.next
        oddend = head
        
        parity = 1
        while curr:
            # increment the node to traverse the list
            temp = curr.next
            
            # connect a node by skipping the next node
            if curr.next: curr.next = curr.next.next
            
            # store the last odd node
            if parity%2==1:
                oddend = curr
                
            # increment parity each turn
            parity += 1
            
            curr = temp
        
        # attach the odd end to the even head
        oddend.next = evenhead
        
        return head