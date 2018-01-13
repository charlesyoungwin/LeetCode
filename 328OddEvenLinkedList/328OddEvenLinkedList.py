# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        odd = head
        even = head.next
        evenHead = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenHead
        return head     

if __name__ == '__main__':

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = None
    Solution().oddEvenList(head)
    while head:
        print(head.val, end = " ")
        head = head.next
    print()