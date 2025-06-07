# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Add two numbers represented by reversed linked lists.
        """
        # Dummy head to simplify edge cases
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Loop until both lists and carry are exhausted
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry, digit = divmod(v1 + v2 + carry, 10)

            current.next = ListNode(digit)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
