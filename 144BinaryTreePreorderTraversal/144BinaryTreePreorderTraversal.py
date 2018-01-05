# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    #recursive
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def traverse(root):
            if not root:
                return
            res.append(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return res
    
    #iterative
    def preorderTraversalV2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        stack.append(root)
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print("solution1:")
    print(Solution().preorderTraversal(root))
    print("solution2:")
    print(Solution().preorderTraversalV2(root))
