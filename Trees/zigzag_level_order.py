

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        res =[]
        queue.append(root)
        counter = True
        while queue:
            n = len(queue)
            levels =[]
            for i in range(n):
                node = queue.popleft()
                levels.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right) 
            if levels and counter:
                res.append(levels)
            if levels and not counter:
                res.append(levels[::-1])      
            counter = not counter
        return res

        
        

# https://leetcode.com/problems/symmetric-tree/submissions/1270316408/