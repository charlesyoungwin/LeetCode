# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root1 = l1
        res1 = 0
        while root1:
            res1 = res1 * 10 + root1.val
            root1 = root1.next
        root2 = l2
        res2 = 0
        while root2:
            res2 = res2 * 10 + root2.val
            root2 = root2.next
        res = res1 + res2
        res = str(res)
        root = ListNode(int(res[0]))
        node = root
        for i in range(1, len(res)):
            root.next = ListNode(int(res[i]))
            root = root.next
        root.next = None
        root = node
        return root

if __name__ == '__main__':
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    root = Solution().addTwoNumbers(l1, l2)
    while root:
        print(root.val, end=" ")
        root = root.next