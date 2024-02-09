# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root : return []
        queue = deque([root])
        ans = []
        while queue :
            tmp, q_size = [], len(queue)
            for _ in range(q_size) :
                cur = queue.popleft()
                tmp.append(cur.val)
                if cur.left : queue.append(cur.left)
                if cur.right : queue.append(cur.right)
            ans.append(tmp)
            
        return ans


        