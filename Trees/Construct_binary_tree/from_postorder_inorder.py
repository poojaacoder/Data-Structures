class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return 

        root_val = postorder.pop()
        root = TreeNode(root_val)
        mid = inorder.index(root_val)
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        return root
    
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/