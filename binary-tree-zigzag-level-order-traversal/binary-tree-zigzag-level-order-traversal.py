# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        from collections import deque
        if not root : return []
        myq, is_reverse = deque([root]), False
        ans = []
        while myq :
            nds = []
            for i in range(len(myq)) :
                curnode = myq.popleft()
                nds.append(curnode.val)
                if curnode.left : myq.append(curnode.left)
                if curnode.right : myq.append(curnode.right)
            if not is_reverse :
                ans.append(nds)
                is_reverse = True
            else :
                ans.append(nds[::-1])
                is_reverse = False
        return ans