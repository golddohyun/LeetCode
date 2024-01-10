class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        adj_list = [[] for _ in range(n+1)]
        delaytime = [0 for _ in range(n+1)]
        for i in times :
            adj_list[i[0]].append((i[1:]))

        queue = deque([k])
        delaytime[k] = 1

        while queue :
            v = queue.popleft()
            for nei, weight in adj_list[v] :
                # update delay time if the new delay time is less than the current
                if delaytime[nei] !=0:
                    if delaytime[nei] > delaytime[v] + weight :
                        delaytime[nei] = delaytime[v] + weight
                    else : continue
                queue.append(nei)
                delaytime[nei] = delaytime[v] + weight
                        
        if 0 in delaytime[1:] : 
            return -1 
        else :
            return max(delaytime[1:])-1
