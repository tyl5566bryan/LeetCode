# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        cur = None
        carry = 0
        
        while l1 != None and l2 != None:
            n = ListNode((l1.val + l2.val + carry) % 10)
            if head == None: head = n
            else: cur.next = n
            cur = n
            carry = (l1.val + l2.val + carry) / 10
            l1 = l1.next
            l2 = l2.next
        
        while carry != 0:
            if l1 == None and l2 == None:
                n = ListNode(carry)
                cur.next = n
                return head
            elif l1 != None:
                n = ListNode((l1.val + carry) % 10)
                cur.next = n
                cur = n
                carry = (l1.val + carry) / 10
                l1 = l1.next
            else:
                n = ListNode((l2.val + carry) % 10)
                cur.next = n
                cur = n
                carry = (l2.val + carry) / 10
                l2 = l2.next
        
        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2
        
        return head
        
                
            
            
            
            
