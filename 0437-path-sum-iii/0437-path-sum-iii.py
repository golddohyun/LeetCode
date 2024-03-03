# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self) :
        self.sumnum = 0

    def backtrack(self, curnode, target, arr) :
        if curnode == None : return 
        arr.append(curnode.val)

        temp_sum = 0
        for i in range(len(arr)-1, -1, -1) :
            temp_sum+=arr[i]
            if temp_sum == target :
                self.sumnum+=1

        if curnode.left : self.backtrack(curnode.left, target, arr)
        if curnode.right  : self.backtrack(curnode.right, target, arr)
        arr.pop()
        
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.backtrack(root, targetSum, [])
        return self.sumnum
        