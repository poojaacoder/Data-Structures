# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        cur = head
        length = 0
        while cur:
            length +=1
            cur = cur.next
        
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        for _ in range(length // k):
            for _ in range(k-1):
                nsxt = cur.next
                cur.next = nsxt.next
                nsxt.next = prev.next
                prev.next = nsxt
            prev = cur
            cur = cur.next

        return dummy.next


# /https://leetcode.com/problems/reverse-nodes-in-k-group/description/?envType=study-plan-v2&envId=top-interview-150
# https://walkccc.me/LeetCode/problems/25/#__tabbed_2_3