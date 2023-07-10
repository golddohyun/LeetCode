class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        if root.left is None and root.right is None :
            return 1

        # if left node is null, recur from the right node
        if root.left is None :
            return self.minDepth(root.right)+1

        # if right node is null, recur from the left node
        if root.right is None :
            return self.minDepth(root.left)+1

        # if no null nodes in depth 2
        return min(self.minDepth(root.left), self.minDepth(root.right))+1