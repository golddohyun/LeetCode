# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root : return []
        ans = []
        queue = deque([root])
        while queue :
            size_ = len(queue)
            curmax = float('-inf')
            for _ in range(size_) :
                curnode = queue.popleft()
                if curnode.val > curmax :
                    curmax = curnode.val
                if curnode.left : queue.append(curnode.left)
                if curnode.right : queue.append(curnode.right)
            ans.append(curmax)
        return ans