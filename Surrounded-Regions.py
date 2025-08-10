class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        if not grid or not grid[0]:
            return

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 'O':
                return
            grid[r][c] = 'S'  # temporarily mark safe
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Run DFS from border cells
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        # 2. Flip surrounded O → X, and safe S → O
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'O':
                    grid[r][c] = 'X'
                elif grid[r][c] == 'S':
                    grid[r][c] = 'O'
