# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def get_childs(parents) :
            gc = []
            for node in parents :
                if node.left : gc.append(node.left.val)
                if node.right : gc.append(node.right.val)
            return gc

        q = deque([root])
        ans = []
        while q :
            curnode = q.popleft()
            if curnode.val % 2 == 0 : 
                parents = []
                if curnode.left : parents.append(curnode.left)
                if curnode.right : parents.append(curnode.right)
                ans+= get_childs(parents)
            if curnode.left : q.append(curnode.left)
            if curnode.right : q.append(curnode.right)

        if not ans : return 0
        return sum(ans)
