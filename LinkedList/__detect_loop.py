class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
 
def printList(head):
    curr = head
    while curr:
        print(curr.data, end=' —> ')
        curr = curr.next
    print('None')
 
 
def removeCycle(head):
    prev = None        
    curr = head        
    s = set()
    while curr:
        if curr in s:
            prev.next = None
            return

        s.add(curr)
        prev = curr
        curr = curr.next
 
if __name__ == '__main__':
 
    head = None
    head = Node(1, head)
    head = Node(0, head)
    head = Node(3, head)
    head = Node(0, head)
    head = Node(1, head)
 
    head.next.next.next.next.next = head.next
 
    removeCycle(head)
    printList(head)