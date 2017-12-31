import collections

class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


class Solution:


    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        dummy, dummy.left = TreeNode(None), root
        row = [dummy]
        #为什么大神们都这么优秀, 什么时候才能到达这个水平
        for _ in range(d - 1):
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        for node in row:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right
        return dummy.left

    #dfs with helper
    def addOneRowDfs(self, root, v, d):
        if not root:
            return
        def dfs(root, depth, v, d):
            if not root:
                return
            if depth < d - 1:
                dfs(root.left, depth + 1, v, d)
                dfs(root.right, depth + 1, v, d)
            else:
                root.left, root.left.left = TreeNode(v), root.left
                root.right, root.right.right = TreeNode(v), root.right
        if d == 1:
            tmp = TreeNode(v)
            tmp.left = root
            return tmp

        dfs(root, 1, v, d)
        return root

    #dfs without helper
    def addOneRowDfs2(self, root, v, d):
        if d == 0 or d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root if d == 1 else None
            newRoot.right = root if d == 0 else None
            return newRoot
        if root and d >= 2:
            root.left = self.addOneRowDfs2(root.left, v, d - 1 if d > 2 else 1)
            root.right = self.addOneRowDfs2(root.right, v, d - 1 if d > 2 else 0)
        return root

def printTreeNode(root):
    #bfs
    if not root:
        return "error"
    res = []
    queue = collections.deque()
    queue.append(root)
    while queue:
        i = 0
        length = len(queue)
        subList = []
        while i < length:
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            i += 1
            subList.append(cur.val)
        res.append(subList)
    for item in res:
        for elem in item:
            print(elem, end=" ")
        print()

def getHeight(root):
    if not root:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))

# 受到启发, 层次遍历的又一种写法
def printTreeNode2(root):
    dummy, dummy.left = TreeNode(None), root
    rows = [dummy]
    for _ in range(getHeight(root)):
        rows = [kid for node in rows for kid in (node.left, node.right) if kid]
        for item in rows:
            print(item.val, end=" ")
        print()




if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(7)
    printTreeNode(root)
    print("--------------------------")
    solu = Solution()
    dummy = solu.addOneRowDfs(root, 9, 3)
    printTreeNode2(dummy)


