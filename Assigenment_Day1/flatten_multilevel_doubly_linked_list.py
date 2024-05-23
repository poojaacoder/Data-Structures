"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        stack = []
        curr = head
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
            elif not curr.next and stack:
                curr.next = stack.pop()
                curr.next.prev = curr
            curr = curr.next
        return head




            




# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/submissions/1262167600/