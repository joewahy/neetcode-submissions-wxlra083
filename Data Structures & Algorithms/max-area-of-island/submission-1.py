class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        directions = [[-1 , 0], [1, 0], [0, -1], [0, 1]]

        def search(r, c):
            if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]) or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            total = 1
            for row, col in directions:
                total += search(r + row, c + col)
            return total

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    result = max(search(row, col), result)
        return result