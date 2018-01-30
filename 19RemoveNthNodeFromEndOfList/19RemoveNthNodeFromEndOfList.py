# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    #two pointers
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        slow = dummy
        fast = dummy
        dummy.next = head
        for i in range(n+1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = None

    head = Solution().removeNthFromEnd(head, 1)
    while head:
        print(head.val, end = " ")
        head = head.next
