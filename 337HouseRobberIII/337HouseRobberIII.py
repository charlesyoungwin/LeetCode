# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    #wrong answer, 没有理解题目的意思
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if not root:
        #     return 
        # import collections
        # queue = collections.deque()
        # queue.append(root)
        # res = []
        # while queue:
        #     size = len(queue)            
        #     tmp = queue.popleft()
        #     res.append(tmp.val)
        #     if tmp.left:
        #         queue.append(tmp.left)
        #     if tmp.right:
        #         queue.append(tmp.right)

        # def helper(ans, index):
        #     if index >= len(ans):
        #         return 0
        #     return max(helper(ans, index + 1), \
        #         ans[index] + helper(ans, index + 2))

        # return helper(res, 0)

        #time exceeded
        if not root:
            return 0
        val = 0
        if root.left:
            val += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)
        return max(val + root.val, self.rob(root.left) + self.rob(root.right))
    
    # ac dp solution
    def robV2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = {}
        def helper(root):
            if not root:
                return 0
            val = 0
            if root in res:
                return res[root]
            if root.left:
                val += helper(root.left.left) + helper(root.left.right)
            if root.right:
                val += helper(root.right.left) + helper(root.right.right)
            value = max(val + root.val, helper(root.left) + helper(root.right))
            res[root] = value
            return value
        return helper(root)

    # greedy solution
    def robV3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root):
            if not root:
                return (0, 0)
            l = helper(root.left)
            r = helper(root.right)
            return (max(l[0], l[1]) + max(r[0], r[1]) , root.val + l[0] + r[0])
        res = helper(root)
        return max(res)

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    print(Solution().robV3(root))