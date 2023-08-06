class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reversed_head = self.reverse_ll(head)
        prev = None
        curr = reversed_head

        for _ in range(n - 1):
            prev = curr
            curr = curr.next
        if prev != None:
            prev.next = curr.next
        else:
            reversed_head = curr.next
        return self.reverse_ll(reversed_head)

    def reverse_ll(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = copy.deepcopy(head)
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
