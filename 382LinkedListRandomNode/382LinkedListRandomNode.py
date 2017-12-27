# Definition for singly-linked list.

import random

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# not ac 没有理解题目意思，未能深入理解概率
class Solution:
    listNode = []

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        root = head
        while root:
            self.listNode.append(root.val)
            root = root.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        length = len(self.listNode)
        return self.listNode[random.randint(0, length - 1)]

#ac
class Solution2:


    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.headNode = head


    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        c = self.headNode
        r = c.val
        i = 1
        while c.next:
            c = c.next
            if random.randint(0, i) == i:
                r = c.val
            i += 1
        return r

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    solu = Solution2(head)
    print(solu.getRandom())