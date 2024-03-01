# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        def find_all_path_src_target(dist, arr, result, k, start) :
            if dist == k:
                print(arr)
                result.append(arr[-1])
                return
            
            for nei in adj_list[start] :
                if not visited[nei] :
                    visited[nei] = 1
                    arr.append(nei)
                    find_all_path_src_target(dist+1, arr, result, k, nei)
                    arr.pop()
                    visited[nei] = 0

        ## Get adjacent List
        queue = deque([root])
        adj_list = defaultdict(list)
        while queue :
            cur = queue.popleft()
            if cur.val not in adj_list :
                adj_list[cur.val] = []
            if cur.left :            
                adj_list[cur.val].append(cur.left.val)
                adj_list[cur.left.val].append(cur.val)            
                queue.append(cur.left)
            if cur.right :
                adj_list[cur.val].append(cur.right.val)
                adj_list[cur.right.val].append(cur.val)
                queue.append(cur.right)


        visited = {key : 0 for key in adj_list.keys()}
        visited[target.val] =1
        result = []
        find_all_path_src_target(0, [target.val], result, k, target.val)
        return result