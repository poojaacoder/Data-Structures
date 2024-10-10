# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        isLoop = False
        if not head :
            return 
        slow = fast = head
        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next
            if slow == fast:
                isLoop = True
                break
        if not isLoop:
            return 
        slow2 = head
        while slow.next:
            if slow == slow2: return slow
            slow = slow.next
            slow2 = slow2.next
        return 
    
        

        
# https://leetcode.com/problems/linked-list-cycle-ii/