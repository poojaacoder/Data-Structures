class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

def Inorder(tree, arr=[]):
    if tree is not None:
        Inorder(tree.left, arr)
        arr.append(tree.val)
        Inorder(tree.right,arr)
    return arr

def Preorder(tree, arr=[]):
    if tree is not None:
        arr.append(tree.val)
        Preorder(tree.left, arr)
        Preorder(tree.right,arr)
    return arr

def Postorder(tree, arr=[]):
    if tree is not None:
        Postorder(tree.left, arr)
        Postorder(tree.right,arr)
        arr.append(tree.val)
    return arr

node1 = BinaryTree(10)
node2 = BinaryTree(12)
node3= BinaryTree(15)
node4 = BinaryTree(20)
node5 = BinaryTree(25)
node1.left = node2
node1.right = node3
node2.left = node4
node3.right = node5

print(Inorder(node1))
print(Postorder(node1))
print(Preorder(node1))