class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def pathsum(node):
            nonlocal res 
            if not node:
                return 0
            
            l = max(0, pathsum(node.left))
            r = max(0, pathsum(node.right))

            res = max(res, node.val+ l+ r)
            return node.val + max(l, r)

        pathsum(root)
        return res
    
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/