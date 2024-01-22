# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root) :
        if not root :
            return []
        queue = deque([root])
        ans = []
        while queue :
            size = len(queue)
            for idx in range(size) :
                v = queue.popleft()
                if idx == size-1 :
                    ans.append(v.val)
                if v.left : queue.append(v.left)
                if v.right : queue.append(v.right)
        return ans