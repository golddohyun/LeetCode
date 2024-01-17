# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sm = [0]
        def cal(r,level):
            if len(sm)<level:
                sm.append(0)
            sm[level-1]+=r.val
            if r.right:
                cal(r.right,level+1)
            if r.left:
                cal(r.left,level+1)
        cal(root,1)
        mx=max(sm)
        for idx, x in enumerate(sm):
            if x == mx:
                return idx+1
