# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def my_soln_addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # O(m + n + max(m, n))
    # get the first number
    num1 = ''
    curr = l1
    while curr:
        num1 += str(curr.val)
        curr = curr.next
    num1 = int(num1[::-1])
    
    # get the second number (same as above)
    num2 = ''
    curr = l2
    while curr:
        num2 += str(curr.val)
        curr = curr.next
    num2 = int(num2[::-1])
    
    # add the numbers
    tot = num1 + num2
    tot = str(tot)[::-1]
    
    # create the linked list
    l = ListNode(val = int(tot[0]))
    curr = l
    for char in tot[1:]:
        curr.next = ListNode(val = int(char))
        curr = curr.next
    
    return l


def one_pass_addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # O(max(m, n))
    curr1 = l1
    curr2 = l2
    
    ans = ListNode()
    var = ans
    carry = 0
    while curr1 or curr2:
        t = (curr1.val if curr1 else 0) + (curr2.val if curr2 else 0) + carry
        var.val = t%10
        carry = t//10
        
        if curr1: curr1 = curr1.next
        if curr2: curr2 = curr2.next
        
        if curr1 or curr2:
            var.next = ListNode()
            var = var.next
    
    if carry:
        var.next = ListNode(val = carry)

    return ans