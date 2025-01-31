from collections import defaultdict
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, index):
            """Performs DFS to calculate island area and marks cells with an island index."""
            stack = [(i, j)]
            grid[i][j] = index
            area = 0
            
            while stack:
                x, y = stack.pop()
                area += 1
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = index
                        stack.append((nx, ny))
            
            return area
        
        m, n = len(grid), len(grid[0])
        island_sizes = {0: 0}  # Dictionary mapping island index to its area
        index = 2  # Start island indices from 2 to avoid confusion with water (0) and land (1)
        
        # Step 1: Identify all islands and calculate their areas
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[index] = dfs(i, j, index)
                    index += 1
        
        # Step 2: Try converting each water cell into land and compute possible largest island
        max_area = max(island_sizes.values(), default=0)  # Largest single island without conversion
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    new_area = 1  # Include the newly converted cell
                    
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > 1:
                            seen.add(grid[ni][nj])
                    
                    new_area += sum(island_sizes[idx] for idx in seen)
                    max_area = max(max_area, new_area)
        
        return max_area if max_area else m * n