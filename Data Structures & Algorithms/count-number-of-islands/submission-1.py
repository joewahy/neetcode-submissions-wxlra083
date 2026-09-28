class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def recursive(r, c):
            if r > 0 and grid[r-1][c] == "1":
                grid[r-1][c] = "0"
                recursive(r - 1, c)
                
            if r < len(grid) - 1 and grid[r+1][c] == "1":
                grid[r+1][c] = "0"
                recursive(r + 1, c)

            if c > 0 and grid[r][c - 1] == "1":
                grid[r][c - 1] = "0"
                recursive(r, c - 1)
            
            if c < len(grid[r]) - 1 and grid[r][c + 1] == "1":
                grid[r][c + 1] = "0"
                recursive(r, c + 1)

        islands = 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == "1":
                    recursive(row, column)
                    islands += 1
        
        return islands
