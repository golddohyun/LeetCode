# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ptr_tmp, length = head, 0

        ## Go to the end of the linked list
        while ptr_tmp :
            ptr_tmp = ptr_tmp.next
            length += 1
        ## Edge case 
        if length == n : return head.next
        ## Second pointer
        ptr = head
        for i in range(length - n -1) :
            ptr = ptr.next
        ptr.next = ptr.next.next
        return head