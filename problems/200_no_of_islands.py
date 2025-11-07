from typing import List
from collections import deque


class Solution:
    def dfs(self, grid: List[List[str]], visited, m, n, i, j) -> int:
        queue = deque()

        queue.append((i, j))
        visited.add((i, j))
        
        while queue:
            i, j = queue.popleft()
            grid[i][j] = "X"
            
            if i + 1 < m and grid[i + 1][j] == "1" and (i + 1, j) not in visited:
                queue.append((i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < n and grid[i][j + 1] == "1" and (i, j + 1) not in visited:
                queue.append((i, j + 1))
                visited.add((i, j + 1))
            if i - 1 >= 0 and grid[i - 1][j] == "1" and (i - 1, j) not in visited:
                queue.append((i - 1, j))
                visited.add((i - 1, j))
            if j - 1 >= 0 and grid[i][j - 1] == "1" and (i, j - 1) not in visited:
                queue.append((i, j - 1))
                visited.add((i, j - 1))
        
        return grid, visited
            
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()

        k = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    grid, visited = self.dfs(grid, visited, m, n, i, j)
                    k += 1
        
        return k

if __name__ == "__main__":
    grid_1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    grid_2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    s = Solution()
    o = s.numIslands(grid_2)
    print(o)
