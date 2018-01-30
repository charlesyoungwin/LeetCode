# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nodeList = []
        tmp = head
        while tmp:
            nodeList.append(tmp.val)
            tmp = tmp.next

        root = self.helper(0, len(nodeList) - 1, nodeList)
        return root
        
    def helper(self, start, end, nodeList):
        if start > end:
            return None
        if start == end:
            return TreeNode(nodeList[start])
        mid = (start + end) // 2
        root = TreeNode(nodeList[mid])
        root.left = self.helper(start, mid - 1, nodeList)
        root.right = self.helper( mid + 1, end, nodeList)
        return root

if __name__ == '__main__':
    head = ListNode(-10)
    head.next = ListNode(-3)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(9)
    head.next.next.next.next.next = None

    root = Solution().sortedListToBST(head)

    print(root)
    