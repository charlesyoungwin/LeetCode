# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if self.checkFirstK(head, k):
            return head

        prev = head
        for i in range(k - 1):
            prev = prev.next 
        prev.next = self.reverseKGroup(prev.next, k)
        newHead = prev
        #   reverse head to prev
        # dummy = ListNode(0)
        # dummy.next = head
        # start = head
        # then = start.next
        # for i in range(k - 1):
        #     start.next = then.next
        #     then.next = dummy.next
        #     dummy.next = then
        #     then = start.next

        ###########
        # another version
        pre = prev.next
        start = head
        for i in range(k):
            temp = start.next
            start.next = pre
            pre = start
            start = temp

        return newHead

    def checkFirstK(self, head, k):
        flag = 0
        for i in range(k):
            if not head:
                flag = 1
                break
            head = head.next
        return flag





def generateLinkedList(nodeList):
    if not nodeList:
        return None
    node = ListNode(nodeList[0])
    node.next = generateLinkedList(nodeList[1:])
    return node

if __name__ == '__main__':
    nodeList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    head = generateLinkedList(nodeList)

    newHead = Solution().reverseKGroup(head, 3)

    while newHead:
        print(newHead.val, end=" ")
        newHead = newHead.next
    print()