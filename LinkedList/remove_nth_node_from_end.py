# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        cur = head
        length = 1
        while cur:
            length +=1
            cur = cur.next
        ele_del = length - n
        print(ele_del)
        #  first element 
        if ele_del ==1 :
            return head.next
        
        #  last element
        if length == ele_del:
            cur = head
            while cur.next:
                cur = cur.next
            cur.next = None
            return head
        #  midd element

        cur = dummy = head
        for i in range(ele_del-2):
            cur = cur.next
        cur.next = cur.next.next

        return head
        


        
       
        
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/