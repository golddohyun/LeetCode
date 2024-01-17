# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        min_level, max_sum = 1, -float('inf')
        q, level = [root], 1
        while q:
            tmp, sum_ = [], 0
            for node in q:
                sum_ += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if sum_ > max_sum:
                min_level, max_sum = level, sum_
            q, level = tmp, level+1
        return min_level