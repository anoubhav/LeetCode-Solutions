# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3290/

import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def middleNode(head):
    # When traversing the list with a pointer slow, make another pointer fast that traverses twice as fast. When fast reaches the end of the list, slow must be in the middle.
    # Time complexity O(N), space O(1)

        slow, fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow



    
