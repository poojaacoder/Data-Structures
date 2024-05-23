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
        que = deque()

        cur = head
        while cur:
            que.append(cur)
            cur= cur.next

        even = False
        dummy = ListNode(0)
        cur = dummy

        while que:
            temp = que.pop() if even else que.popleft()
            temp.next = None
            cur.next = temp
            cur = cur.next
            even ^= True

        return dummy.next



        # https://leetcode.com/problems/reorder-list/submissions/1264708976/
    # https://www.youtube.com/watch?v=XIJMdQUzs-I