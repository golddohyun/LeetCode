class Solution:
    def maximumDetonation(self, B):
        from collections import defaultdict, deque

        if len(B) == 1 : return 1
        adj_list, lenb = dict(), len(B)

        # Get adjacenty list for the bombs
        for i in range(lenb) :
            for j in range(lenb) :
                if i == j : continue
                if i not in adj_list :
                    adj_list[i] = []
                dist_range = B[i][2]
                if ((B[i][0]-B[j][0])**2 + (B[i][1]-B[j][1])**2) <= (dist_range**2) :
                    adj_list[i].append(j)


        max_cnt , queue = 0, deque()
        for b in adj_list : 
            cnt, used = 0, [0]*lenb
            queue.append(b)
            used[b] = 1
            while queue :
                cur = queue.popleft()
                cnt+=1
                for nei in adj_list[cur] :
                    if not used[nei]:
                        queue.append(nei)
                        used[nei] = 1

            if max_cnt < cnt :
                max_cnt = cnt
        return max_cnt