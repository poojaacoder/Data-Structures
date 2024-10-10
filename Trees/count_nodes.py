class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left + right + 1
    

# https://leetcode.com/problems/count-complete-tree-nodes/