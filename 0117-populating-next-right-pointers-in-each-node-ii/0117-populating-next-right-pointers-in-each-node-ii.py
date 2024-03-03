"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):    
        if not root : return None    
        from collections import deque
        Q = deque([root])
        while Q :
            size = len(Q)
            for n in range(size) :
                curnode = Q.popleft()
                if n == size-1 :
                    curnode.next = None
                else :
                    curnode.next = Q[0]
                if curnode.left : Q.append(curnode.left)
                if curnode.right : Q.append(curnode.right)
        return root