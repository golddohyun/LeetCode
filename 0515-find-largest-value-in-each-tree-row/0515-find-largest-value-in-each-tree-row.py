# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans =[]
        if root is None : return
        queue = [root]
        
        while (len(queue) > 0) :
            size = len(queue)
            max_num = float('-inf')
            for _ in range(size):
                node = queue.pop(0)
                max_num = max(max_num, node.val)
                if node.left : queue.append(node.left)
                if node.right : queue.append(node.right)
            ans.append(max_num)
        return ans