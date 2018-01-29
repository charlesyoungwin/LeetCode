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
        head = self.helper(head)
        return head
        


    def helper(self, head):
        if not head or not head.next:
            return head
        newHead = head.next       
        head.next = newHead.next
        newHead.next = head
        head.next = self.helper(head.next)
        return newHead

    #solution2 
    def swapPairsV2(self, head):
        if not head: return None
        p1, p2 = head, head.next
        while p2:
            p1.val, p2.val = p2.val, p1.val
            p1 = p2.next
            p2 = p1.next if p1 else p1
        return head

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = None
    head = Solution().swapPairsV2(head)
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


