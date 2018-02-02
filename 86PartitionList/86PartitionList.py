# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #solution 1
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy2 = ListNode(0)
        prev = dummy
        largeLinkNode = dummy2
        dummy.next = head
        cur = head
        while cur:
            if cur.val >= x:
                largeLinkNode.next = cur
                largeLinkNode = largeLinkNode.next
                prev.next = cur.next
                cur = cur.next
            else:
                prev = prev.next
                cur = cur.next
        largeLinkNode.next = None
        prev.next = dummy2.next
        return dummy.next

    #solution 2
    def partitionV2(self, head, x):
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next

def generateLinkedList(nums):
    if not nums:
        return None
    node = ListNode(nums[0])
    node.next = generateLinkedList(nums[1:])
    return node

if __name__ == '__main__':
    nodeList = [1, 4, 3, 2, 5, 2]
    head = generateLinkedList(nodeList)
    newHead = Solution().partitionV2(head, 3)
    while newHead:
        print(newHead.val, end=" ")
        newHead = newHead.next
    print()

