
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def mergeSortedList(self, l1, l2):
        result = Node(0)
        head = result
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1= l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        if l1:
            head.next = l1
        else:
            head.next = l2

        return result.next
    
    def printList(self, head):
        cur = head
        while cur:
            print(cur.val)
            cur= cur.next

    

list1 = Node(10)
list1.next = Node(12)
list1.next.next= Node(15)

s = Solution()
print("first list")
s.printList(list1)

list2 = Node(11)
list2.next = Node(13)
list2.next.next= Node(14)
list2.next.next.next = Node(20)
list2.next.next.next.next = Node(26)
list2.next.next.next.next.next = Node(40)

list2 = Node(11)
head2 = list2
k = [13, 14, 20,26,40]
for i in range(5):
    head2.next = Node(k[i])
    head2 = head2.next
print("second list")
s.printList(list2)

list3 = s.mergeSortedList(list1, list2)
print("third list")
s.printList(list3)




