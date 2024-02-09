# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root : return []
        level = {}
        queue = deque([root])
        ans, lv = [], 0
        while queue :
            q_size = len(queue)
            if lv not in level : level[lv] = []
            for _ in range(q_size) :
                cur = queue.popleft()
                level[lv].append(cur.val)
                if cur.left : queue.append(cur.left)
                if cur.right : queue.append(cur.right)
            lv+=1
        for k, v in sorted(level.items(), reverse=True) :
            ans.append(v)
        return ans
