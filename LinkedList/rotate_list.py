# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
 1 -> 2 -> 3 -> 4
get n 
list 1 -> none  + list 2 -> 
list 2 -> None -> head

return list2

"""
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        l = 1
        cur = head 
        while cur.next:
            cur = cur.next
            l +=1
        cur.next = head
 
        mid = (l - k )% l
        print(mid)

        for i in range(mid):
            cur = cur.next
        ns = cur.next
        cur.next = None

        return ns
        

        