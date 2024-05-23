class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def addTwoIntegers(self, l1, l2):
        head = Node(0)
        root = head.next
        carry = 0

        while l1 and l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1+ v2 + carry

            carry = sum // 10
            head.next = Node(sum % 10)
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return root.next
    

    #  time complexity max(m, n)
#  m length of l1 and n length of l2
    #  space complexity : max(m, n) + 2 = max(m,n)
    #  we drop constants for calculating complexity

        

            





        
        