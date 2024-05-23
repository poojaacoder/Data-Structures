

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.random = None

def copy_random_pointer_list(head):

    if not head :
        return head
    cur = head
    dummy = Node(-1)
    dummy.next = head
    # insert new node 
    while cur:
        temp = Node(cur.val)
        temp.next = cur.next
        cur.next = temp
        cur = temp.next


    # update random pointer
    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next

    cur = dummy
    old = head

    while old:
        cur.next = old.next
        cur = old
        old = cur.next


    return dummy.next

#  O(n) time complexity

    # update new list for random pointers
