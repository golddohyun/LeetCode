# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head : return head
        dummy = ListNode(0, next=head)
        prev, cur, next = dummy, head, head.next
        while cur and cur.next : 
            prev.next, cur.next = next, next.next
            next.next = cur
            if cur and cur.next :
                prev, cur, next = cur, cur.next, cur.next.next
        return dummy.next

