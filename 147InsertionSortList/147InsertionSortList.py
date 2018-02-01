# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #solution 1
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = dummy = ListNode(0)
        while head:
            if cur and cur.val > head.val:
                cur = dummy
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, cur.next.next, head = head, cur.next, head.next
        return dummy.next

def generateLinkedList(nums):
    if not nums:
        return None
    node = ListNode(nums[0])
    node.next = generateLinkedList(nums[1:])
    return node

if __name__ == '__main__':
    nums = [1, 3, 2]
    head = generateLinkedList(nums)
    newHead = Solution().insertionSortList(head)
    while newHead:
        print(newHead.val, end=" ")
        newHead = newHead.next
    print()