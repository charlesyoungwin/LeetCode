# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #solution1: partion solution 
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return self.partion(lists, 0, len(lists) - 1)

    def partion(self, lists, s, e):
        if s == e:
            return lists[s]
        elif s < e:
            m = (s + e) // 2
            l1 = self.partion(lists, s, m)
            l2 = self.partion(lists, m + 1, e) 
            return self.merge(l1, l2)
        else:
            return None

    def merge(self, listA, listB):
        headA = listA
        headB = listB
        dummy = head = ListNode(0)
        while headA and headB:
            if headA.val <= headB.val:
                head.next = headA
                headA = headA.next
            else:
                head.next = headB
                headB = headB.next
            head = head.next
        if headA:
            head.next = headA
        if headB:
            head.next = headB
        return dummy.next

    #solution2: use priority queue
    
    def mergeKListsV2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import queue
        dummy = ListNode(None)
        curr = dummy
        q = queue.PriorityQueue()
        for idx, node in enumerate(lists):
            if node:
                q.put((node.val, idx, node))
        while q.qsize() > 0:
            poped = q.get()
            curr.next, idx= poped[2], poped[1]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, idx, curr.next))
        return dummy.next



def generateLinkedList(nums):
    if not nums:
        return None
    dummy = head =  ListNode(0)
    for item in nums:
        node = ListNode(item)
        head.next = node
        head = head.next
    return dummy.next

if __name__ == '__main__':
    nums = [[1, 3, 5], [2, 4], [1, 9, 10]]
    lists = []
    for i in range(len(nums)):
        head = generateLinkedList(nums[i])
        lists.append(head)
    newHead = Solution().mergeKListsV2(lists)
    while newHead:
        print(newHead.val, end=" ")
        newHead = newHead.next
    print()
