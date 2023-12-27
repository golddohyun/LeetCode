class Solution(object):
    def getsize(self, head) :
        size = 0
        curnode = head
        while curnode != None :
            size += 1
            curnode = curnode.next
        return size  # Return the computed size

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None or n <= 0:  # Handle edge case
            return head

        size = self.getsize(head)
        if n > size:  # If n is greater than list size, return head
            return head
        if n == size:  # If n is equal to list size, remove first node
            return head.next

        prev, target = None, head
        idx = size - n
        while idx > 0 :
            idx -= 1
            prev = target
            target = target.next
        
        if prev is None:  # If removing the first node
            head = target.next
        else:
            prev.next = target.next

        return head