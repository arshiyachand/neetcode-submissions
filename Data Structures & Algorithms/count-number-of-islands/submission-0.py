class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def setzero(grid, row, col):
            if (0 <= row < len(grid)) and (0 <= col < len(grid[0])) and grid[row][col] == "1":
                grid[row][col] = "0"

                for rowiter, coliter in directions:
                    setzero(grid, row+rowiter, col+coliter)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    numIslands += 1
                    setzero(grid, row, col)
        
        return numIslands