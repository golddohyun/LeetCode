class Solution(object):
    def getsize(self, head) :
        size = 0
        curnode = head
        while curnode != None :
            size += 1
            curnode = curnode.next
        return size

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        prev, cur, length = None, head, self.getsize(head)
        if head is None : return head
        if length == n : return head.next

        for _ in range(length-n) :
            prev, cur = cur, cur.next

        prev.next = cur.next
        return head