# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode(0)
        while l1 and l2:
            value = l1.val + l2.val
            node = ListNode(value % 10 + carry)
            carry = value // 10
            l1 = l1.next
            l2 = l2.next
