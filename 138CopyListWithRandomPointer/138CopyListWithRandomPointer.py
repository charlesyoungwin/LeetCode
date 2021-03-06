# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        node = head
        dic = {}
        while node:
            dic[node] = RandomListNode(node.label)
            node = node.next
        node = head
        while node:
            dic[node].next = dic.get(node.next, None)
            dic[node].random = dic.get(node.random, None)
            node = node.next
        return dic[head]


        