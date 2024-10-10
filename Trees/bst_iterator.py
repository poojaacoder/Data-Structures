class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.inorder(root)
        
    def inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        root = self.stack.pop()
        self.inorder(root.right)
        return root.val


    def hasNext(self) -> bool:
        return self.stack
        



# https://leetcode.com/problems/binary-search-tree-iterator/