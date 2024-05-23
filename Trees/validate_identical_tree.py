from collections import deque
class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def identical(root1, root2):
    if root1 == None and root2 == None:
        return True
    
    if root1.val == root2.val and \
        identical(root1.left, root2.left) and  identical(root1.right , root2.right):
        return True
    else:
        return False

node1 = Tree(10)
node2 = Tree(12)
node3= Tree(15)
node4 = Tree(20)
node5 = Tree(25)
node1.left = node2
node1.right = node3
node2.left = node4
node3.right = node5


nodea = Tree(1)
nodeb = Tree(12)
nodec= Tree(15)
noded = Tree(20)
nodee = Tree(25)
nodea.left = nodeb
nodea.right = nodec
nodeb.left = noded
nodec.right = nodee

print(identical(node1, nodea))