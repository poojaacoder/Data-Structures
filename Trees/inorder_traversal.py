class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        arr = []
        def traverse(head, arr):
            if not head:
                return arr
            traverse(head.left, arr)
            arr.append(head.val)
            traverse(head.right, arr)
            return arr

        return traverse(root, arr)
# https://leetcode.com/problems/binary-tree-inorder-traversal/