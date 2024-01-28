# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root):
        sum_dct, maxlevel = dict(), 0
        queue = deque([root])
        while queue :
            tmp, q_size = 0, len(queue)
            for _ in range(q_size) :
                curnode = queue.popleft()
                if curnode.left : queue.append(curnode.left)
                if curnode.right : queue.append(curnode.right)
                tmp += curnode.val
            sum_dct[maxlevel] = tmp
            maxlevel+=1
        # print(sum_dct)
        for lev, num in sum_dct.items() :
            if num == max(sum_dct.values()) :
                return lev +1