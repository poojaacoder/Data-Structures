class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_depth(node):
    if node is  None:
        return 0
    
    ldepth = max_depth(node.left)
    rdepth = max_depth(node.right)

    if ldepth >= rdepth:
        return  ldepth+1
    else:
        return rdepth+1
    
def min_depth(node):
    if node is  None:
        return 0
    
    ldepth = max_depth(node.left)
    rdepth = max_depth(node.right)

    if ldepth <= rdepth:
        return  ldepth+1
    else:
        return rdepth+1

    







node1 = BinaryTree(10)
node2 = BinaryTree(12)
node3= BinaryTree(15)
node4 = BinaryTree(20)
node5 = BinaryTree(25)
node6 = BinaryTree(30)
node1.left = node2
node2.right = node3
node2.left = node4
node3.right = node5
node5.left = node6

print(max_depth(node1))
print(min_depth(node1))

