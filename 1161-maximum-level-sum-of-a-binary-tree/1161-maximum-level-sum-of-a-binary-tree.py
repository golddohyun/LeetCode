# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root):
        sums = []
        queue = deque([root])
        while queue :
            size = len(queue)
            sum = 0
            for _ in range(size) :
                v = queue.popleft()
                sum += v.val
                if v.left : queue.append(v.left)
                if v.right : queue.append(v.right)
            sums.append(sum)
        
        for idx in range(len(sums)) :
            if sums[idx] == max(sums) :
                return idx+1
