# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    #写得太乱了。。。
    def splitListToPartsNotAc(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = 0
        node = root
        rListNode = []
        while not node:
            length += 1
            node = node.next
        if length // k == 0:
            node = root
            while node:
                listNode = ListNode(node.val)
                listNode.next = None
                rListNode.append(listNode)
                node = node.next
            for i in range(0, k - length):
                rListNode.append(None)
        else:
            reminder = length % k
            divider = length // k
            node = root
            while node:
                for i in range(0, len(reminder)):
                    listNode = ListNode(node.val)
                    count = 0
                    while count < divider + 1:
                        listNode.next = node.next
                        listNode = listNode.next
                        node = node.next
                    listNode.next = None
                    rListNode.append(listNode)
                for i in range(0, divider - reminder):
                    listNode = ListNode(node.val)
                    listNode.next = node.next
                    listNode = listNode.next
                    node = node.next
                    listNode.next = None
                    rListNode.append(listNode)
        return rListNode

    def splitListToPartsAc(self, root, k):
        curr, length = root, 0
        while curr:
            curr, length = curr.next, length + 1
        chunk_size, longer_chunks = length // k, length % k
        res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)
        #Split up the list
        prev, curr = None, root
        for index, num in enumerate(res):
            if prev:
                prev.next = None
            res[index] = curr
            for i in range(num):
                prev, curr = curr, curr.next
        return res

if __name__ == '__main__':

    def printListNode(root):
        while root:
            print(root.val, end=" ")
            root = root.next

    root = ListNode(1)
    curr = root
    for i in range(2, 11):
        curr.next = ListNode(i)
        curr = curr.next
    curr.next = None
    solu = Solution()
    for item in solu.splitListToPartsAc(root, 3):
        printListNode(item)
        print("; ")



