# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged =[]
            for i in range(0, len(lists), 2):
                l1= lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged.append(self.mergeList(l1,l2))
            lists = merged
        return lists[0]

    def mergeList(self,l1, l2):

        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 =l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        
        return dummy.next

# https://leetcode.com/problems/merge-k-sorted-lists/description/