# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        length = 0
        start = head
        while start:
            start = start.next
            length += 1
        k = k % length
        if k == 0:
            return head
        slow = fast = head
        while k > 0:
            fast = fast.next
            k -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        newHead = slow.next
        slow.next = None
        fast.next = head
        return newHead

def generateList(nums):
    if not nums:
        return None
    head = start = ListNode(nums[0])
    for i in range(1, len(nums)):
        start.next = ListNode(nums[i])
        start = start.next
    return head

if __name__ == '__main__':
    nums = [1, 2]
    head = generateList(nums)
    newHead = Solution().rotateRight(head, 4)
    while newHead:
        print(newHead.val, end = " ")
        newHead = newHead.next
    print()