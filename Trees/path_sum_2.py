class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node, summ, path):
            summ += node.val
            if node.left:
                dfs(node.left, summ, path +[node.val])
            if node.right:
                dfs(node.right, summ, path + [node.val])
            if not node.left and not node.right and summ == targetSum:
                ans.append(path+[node.val])
        
        if not root: return []
        dfs(root, 0, [])
        return ans
    
# https://leetcode.com/problems/path-sum-ii/