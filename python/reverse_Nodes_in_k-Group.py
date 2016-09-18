# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2:
            return head
        
        L = ListNode(0)
        L.next = head
        pre = L
        
        start, tail, cur_len = head, head, 1
        
        while start and tail:
            while cur_len < k and tail.next:
                tail = tail.next
                cur_len += 1
            if cur_len == k:
                suf = tail.next
                tail.next = None
                (temp_h, temp_t) = self.reverseList(start)
                pre.next, temp_t.next = temp_h, suf
                start, tail, cur_len = suf, suf, 1
                pre = temp_t
            elif not tail.next:
                break
        
    return L.next

def reverseList(self, head):
    p, q = head, head.next
        while q:
            temp = q.next
            q.next = p
            p = q
            q = temp
    head.next = None
        return (p, head)

