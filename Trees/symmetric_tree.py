class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isSame(a, b):
            if not a or not b:
                return a == b
            if a.val == b.val and isSame(a.left, b.right) and isSame(a.right, b.left):
                return True

        return isSame(root, root)
    
# https://leetcode.com/problems/symmetric-tree/submissions/1270316408/