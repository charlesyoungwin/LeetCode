# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #solution 1, time exceeded, not accepted
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow = fast = head
        fast = slow.next
        while fast:
            slow = head
            while slow != fast:
                if slow.val > fast.val:
                    temp = slow.val
                    slow.val = fast.val
                    fast.val = temp
                slow = slow.next
            fast = fast.next
        return head


    #solution 2
    def insertionSortListV2(self, head):
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
            # cur.next.next, cur.next, head = cur.next, head, head.next
        return dummy.next

    
def generateLinkedList(nums):
    if not nums:
        return None
    node = ListNode(nums[0])
    node.next = generateLinkedList(nums[1:])
    return node

if __name__ == '__main__':
    nodeList = [1, 2, 4, 3]
    head = generateLinkedList(nodeList)
    newHead = Solution().insertionSortListV2(head)
    while newHead:
        print(newHead.val, end=" ")
        newHead = newHead.next
    print()