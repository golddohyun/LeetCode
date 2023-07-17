# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Use two stacks to store the number
        stack1 = []
        stack2 = []
        ptr = l1
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        ptr = l2
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        carry = 0
        result = []
        head = ListNode(-1)
        while stack1 or stack2:
            if not stack1:
                val = stack2.pop()
            elif not stack2:
                val = stack1.pop()
            else:
                val = stack1.pop() + stack2.pop()    
            carry, val = divmod(carry + val, 10)
            head.val = val
            temp = head
            head = ListNode(-1)
            head.next = temp
        if carry: head.val = carry
        return head if head.val != -1 else head.next