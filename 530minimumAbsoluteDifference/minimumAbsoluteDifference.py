import random

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Bst():

	def __init__(self):
		self.root = None
		self.size = 0

	def insert(self, treeNode):
		if self.root is None:
			self.root = treeNode
		else:
			current = self.root
			while 1:
				if treeNode.val < current.val:
					if current.left:
						current = current.left
					else:
						current.left = treeNode
						break
				elif treeNode.val > current.val:
					if current.right:
						current = current.right
					else:
						current.right = treeNode
						break
				else:
					break


	def inorderPrint(self, treeNode):
		if treeNode is None:
			return 
		self.inorderPrint(treeNode.left)
		print(treeNode.val, end="  ")
		self.inorderPrint(treeNode.right)

class Solution(object):

	def getMinimumDifference(self, root):
		aList = []
		def visit(node):
			if node is None:
				return
			visit(node.left)
			aList.append(node.val)
			visit(node.right)
		visit(root)
		aList.sort()
		print(aList)
		min = float('inf')
		for i in range(1, len(aList)):
			if aList[i] - aList[i - 1] < min:
				min = aList[i] - aList[i - 1]
		return min

if __name__ == '__main__':
	tree = Bst()
	listA = []
	for i in range(0, 10):
		a = random.randint(0, 20)
		listA.append(a)
		treeNode = TreeNode(a)
		tree.insert(treeNode)
	print(listA)
	print("-------------------")
	solution = Solution()
	print(solution.getMinimumDifference(tree.root))