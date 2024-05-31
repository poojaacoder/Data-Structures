
def countSubTree(root, target):
    def dfs(node, target, counter):
        summ = lsum = rsum = 0
        if node.left:
            lsum = dfs()
        if node.right:
            rsum = dfs()
        summ = lsum + rsum + node.val
        if summ == target: counter +=1
        return summ
    
    counter = 0
    dfs(root, target, counter)
    return counter

