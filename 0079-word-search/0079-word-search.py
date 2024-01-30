## 79. Word Search
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        import copy
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        rows, cols = len(board), len(board[0])
        def dfs(x, y, tmp, lencnt, grid) :
            if lencnt == len(word) :
                # print(''.join(tmp))
                return ''.join(tmp) == word
            for i in range(4) :
                nx, ny = x+dx[i], y+dy[i]
                if (nx < 0 or ny < 0 or nx >= len(grid) or ny >=len(grid[0]) or lencnt == len(word)) : continue
                if (grid[nx][ny] != word[lencnt] or grid[nx][ny] == "#") : continue
                tmp.append(board[nx][ny])
                lencnt+=1
                grid[nx][ny] = "#"
                if dfs(nx, ny, tmp, lencnt, grid) :
                    return True
                tmp.pop()
                lencnt-=1
                grid[nx][ny] = board[nx][ny]
            return False
            
        found = False
        for r in range(rows) :
            for c in range(cols) :
                if board[r][c] == word[0] :
                    grid = copy.deepcopy(board)
                    grid[r][c] = "#"
                    if dfs(r, c, [word[0]], 1, grid) :  
                        found = True
                        break
            if found :
                break
        return found

