class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def reverseList(self, head):
        prev = None
        current = head
        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        current = temp


        # self.printList(prev)
        return prev

    def printList(self,head):
        cur = head
        while cur:
            print(cur.val)
            cur= cur.next


list2 = Node(11)
list2.next = Node(13)
list2.next.next= Node(14)
list2.next.next.next = Node(20)
list2.next.next.next.next = Node(26)
list2.next.next.next.next.next = Node(40)

obj = LinkedList()
# obj.printList(list2)
list3 = obj.reverseList(list2)
obj.printList(list3)




    