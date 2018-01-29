# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = head
        self.helper(start)
        return head


    def helper(self, head):
        if not head or not head.next:
            return head
        tmp = head.next.next
        head.next.next = head
        head.next = tmp
        head.next = self.helper(head.next)
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = None
    head = Solution().swapPairs(head)
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


