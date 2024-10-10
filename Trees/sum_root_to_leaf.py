class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def sumNodes(node, cur_sum):
            if not node:
                return 0
            cur_sum = cur_sum * 10 + node.val
            if not node.right and not node.left:
                return cur_sum
            return sumNodes(node.left, cur_sum) + sumNodes(node.right, cur_sum)
        
        return sumNodes(root, 0)
        

# https://leetcode.com/problems/sum-root-to-leaf-numbers/