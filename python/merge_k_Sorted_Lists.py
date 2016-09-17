# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return []
        
        k = len(lists)
        
        while k > 1:
            i = 0
            while i < k - 1:
                lists[i/2] = self.mergeTwoLists(lists[i], lists[i+1])
                i += 2
            if i == k - 1:
                lists[i/2] = lists[i]
            k = (k + 1) / 2
        
        return lists[0]
        
    
    def mergeTwoLists(self, l1, l2):

        p1, p2 = l1, l2
        head = ListNode(0)
        p = head
        
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p = p1
                p1 = p1.next
            else:
                p.next = p2
                p = p2
                p2 = p2.next
        
        if p1: p.next = p1
        if p2: p.next = p2
        
        return head.next
        