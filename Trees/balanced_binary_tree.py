class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def maxDepth(root) -> int:
            if not root:
                return 0
            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        diff = abs(maxDepth(root.left) - maxDepth(root.right)) <= 1 
        balanced = self.isBalanced(root.left) and self.isBalanced(root.right)
        return diff and balanced