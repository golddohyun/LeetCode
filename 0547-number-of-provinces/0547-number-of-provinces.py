class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        prov = 0
        visited = [0]*len(isConnected)
        for area in range(len(isConnected)) :
            if visited[area] : continue
            visited[area] = 1
            q = deque([area])
            prov+=1
            while q :
                curarea = q.popleft()
                for idx in range(len(isConnected[0])):
                    if curarea != idx and visited[idx] !=1 and isConnected[curarea][idx] == 1 :
                        visited[idx] = 1
                        q.append(idx)
        return prov