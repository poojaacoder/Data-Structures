# Python3 program to find if there is a 
# subtree with given sum 

# Binary Tree Node 
""" utility that allocates a newNode 
with the given key """
class newnode: 

	# Construct to create a newNode 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None

def sumSubtreeUtil(node,cur_sum,sum): 

	# base condition 
	if (node == None): 
		cur_sum[0] = 0
		return False

	sum_left, sum_right = [0], [0] 
	x=sumSubtreeUtil(node.left, sum_left, sum) 
	y=sumSubtreeUtil(node.right, sum_right, sum) 
	print(x, y)
	cur_sum[0] = (sum_left[0] +
				sum_right[0] + node.data)
	print(cur_sum)
	return ((x or y)or (cur_sum[0] == sum)) 

def sumSubtree(root, sum): 

	cur_sum = [0] 

	return sumSubtreeUtil(root, cur_sum, sum) 

# Driver Code 
if __name__ == '__main__': 

	root = newnode(8) 
	root.left = newnode(5) 
	root.right = newnode(4) 
	root.left.left = newnode(9) 
	root.left.right = newnode(7) 
	root.left.right.left = newnode(1) 
	root.left.right.right = newnode(12) 
	root.left.right.right.right = newnode(2) 
	root.right.right = newnode(11) 
	root.right.right.left = newnode(3) 
	sum = 22

	if (sumSubtree(root, sum)) : 
		print("Yes" ) 
	else: 
		print("No") 

# This code is contributed by 
# Shubham Singh(SHUBHAMSINGH10) 
