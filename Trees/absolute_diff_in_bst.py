class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        min_diff = float('inf')
        def inorder(node):
            nonlocal prev, min_diff
            if not node:
                return 
            
            inorder(node.left)
            if prev is not None:
                min_diff = min(min_diff, node.val - prev.val)
            prev = node
            inorder(node.right)

        
        inorder(root)
        return min_diff
    

# https://leetcode.com/problems/minimum-absolute-difference-in-bst/