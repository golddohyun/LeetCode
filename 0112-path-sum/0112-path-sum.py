# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root : return False
        def DFS(curnode, target, arr) :
            if not curnode.left and not curnode.right :
                if sum(arr) == target :
                    print(arr)
                    return True 
                return False

            print("current visit : ", curnode.val, arr)
            if curnode.left :
                if DFS(curnode.left, target, arr+[curnode.left.val]) : return True
            if curnode.right : 
                if DFS(curnode.right, target, arr+[curnode.right.val]) : return True
            return False        
        return DFS(root, targetSum, [root.val])