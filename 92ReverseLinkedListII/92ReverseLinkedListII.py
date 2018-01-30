class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        index = 1
        dummyNode = ListNode(0)
        dummyNode.next = head
        curr = head
        while index < m - 1:
            curr = curr.next
            index += 1
        prev = None
        first = curr
        curr = curr.next
        while index < n:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            index += 1
        first.next.next = curr
        first.next = prev
        return head

    def reverseBetweenV2(self, head, m, n):
        if m == n:
            return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next

        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next
        pre.next.next = cur
        pre.next = reverse
        return dummyNode.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = None

    newHead = Solution().reverseBetween(head, 2, 4)
    while newHead:
        print(newHead.val, end=" ")
        newHead = newHead.next
    






