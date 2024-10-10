class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def inorder(node, arr):
            if not node:
                return
            if len(arr) == k:
                return
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)
        
        arr = []
        inorder(root, arr)
        print(arr)
        return arr[k-1]

https://leetcode.com/problems/kth-smallest-element-in-a-bst/