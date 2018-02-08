# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 
        start = head
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        curr = slow
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode 
        newHead = prev
        while start:
            tmp1 = start.next
            tmp2 = newHead.next
            start.next = newHead
            if tmp1:
                newHead.next = tmp1
            start = tmp1
            newHead = tmp2
        start = newHead
        


def generateLinkedlist(nums):
    if not nums:
        return None
    start = head = ListNode(nums[0])
    for i in range(1, len(nums)):
        start.next = ListNode(nums[i])
        start = start.next
    return head


if __name__ == '__main__':
    
    nums = [1, 2, 3]
    head = generateLinkedlist(nums)
    Solution().reorderList(head)
    while head:
        print(head.val, end = " ")
        head = head.next
    print()