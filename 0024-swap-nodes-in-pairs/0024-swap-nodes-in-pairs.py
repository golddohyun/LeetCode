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
        if not head or head.next is None : return head
        cur = head
        head = head.next
        while cur and cur.next:
            adj = cur.next
            cur.next = adj.next
            adj.next = cur

            # initialize
            tmp = cur.next
            if tmp and tmp.next :
                cur.next = tmp.next
            cur = tmp
        return head

