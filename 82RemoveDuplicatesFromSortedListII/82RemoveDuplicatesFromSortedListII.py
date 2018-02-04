# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev =  dummy
        cur = head
        while cur and cur.next:
            if cur.next.val != cur.val:
                cur = cur.next
                prev = prev.next
            else:
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                prev.next = cur.next
                cur = cur.next
        return dummy.next


def generateLinkedList(nums):
    if not nums:
        return None
    node = ListNode(nums[0])
    node.next = generateLinkedList(nums[1:])
    return node


if __name__ == '__main__':
    nums = [1, 1]
    head = generateLinkedList(nums)
    newHead = Solution().deleteDuplicates(head)
    while newHead:
        print(newHead.val, end=" ")
        newHead = newHead.next
    print()    
