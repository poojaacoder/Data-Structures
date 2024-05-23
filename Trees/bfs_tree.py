from collections import deque
class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs_traverse(root):
    if not root:
        return

    queue = deque()
    queue.append(root)
    result = []
    while queue:
        n = len(queue)
        level = []
        for i in range(n):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level:
            result.append(level)

    return result

node1 = Tree(10)
node2 = Tree(12)
node3= Tree(15)
node4 = Tree(20)
node5 = Tree(25)
node1.left = node2
node1.right = node3
node2.left = node4
node3.right = node5
print(bfs_traverse(node1))
            

        



#  also call level order traveral
# O(n) space and time c
