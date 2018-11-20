# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(l1.val + l2.val)
        l1 = l1.next
        l2 = l2.next
        x = l3
        while l1 or l2 or x.val >= 10:
            y = ListNode(int(x.val/10))
            if l1:
                y.val += l1.val
                l1 = l1.next
            if l2:
                y.val += l2.val
                l2 = l2.next
            x.val %= 10
            x.next = y
            x = y
        return l3
