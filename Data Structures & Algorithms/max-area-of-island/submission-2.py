class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        result = 0

        def area(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + sum(area(r + dr, c + dc) for dr, dc in directions)

        for r in range(rows):
            for c in range(cols):
                result = max(area(r,c), result)
        return result