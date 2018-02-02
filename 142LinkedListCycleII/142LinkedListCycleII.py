# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object): 
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        fast = slow = head
        entry = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry

        return None

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    entry = head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    end = head.next.next.next.next = ListNode(5)
    end.next = entry
    
    
