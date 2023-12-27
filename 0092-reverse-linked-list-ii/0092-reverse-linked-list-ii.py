class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        start = dummy
        
        # save the start and end node info
        for _ in range(left-1):
            start = start.next
        end = start.next
        
        # run the reverse loop for sll
        curnode, prev = start.next, None   
        for _ in range(right - left + 1):
            next_tmp, curnode.next = curnode.next, prev
            prev, curnode = curnode, next_tmp
            
        start.next, end.next = prev, curnode
        
        return dummy.next     
