class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def hasPathSum(root, targetSum):
    def dfs(node, curr_sum):
        if node is None:
            return False      
        curr_sum += node.val

        if node.left is None and node.right is None:
            return  curr_sum == targetSum
        
        return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
    return dfs(root, 0)
        


node1 = Tree(10)
node2 = Tree(12)
node3= Tree(15)
node4 = Tree(20)
node5 = Tree(25)
node1.left = node2
node1.right = node3
node2.left = node4
node3.right = node5
print(hasPathSum(node1, 12))
