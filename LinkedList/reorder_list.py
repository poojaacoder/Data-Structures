# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        # find middle
        slow ,fast = head, head.next
        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next

        
        #  reverse second half

        second  = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        #  merge two lists
        second = prev
        first = head
        while second:
            temp = first.next
            temp2 = second.next
            first.next = second
            second.next = temp
            first = temp
            second = temp2






        # https://leetcode.com/problems/reorder-list/