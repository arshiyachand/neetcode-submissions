class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        def setzero(grid,row, col):
            area = 0
            if (0 <= row < len(grid)) and (0 <= col < len(grid[0])) and grid[row][col] == 1:
                grid[row][col] = 0
                area += 1

                for rowiter, coliter in directions:
                    area += setzero(grid, row+rowiter, col + coliter)
            return area


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxarea = max(maxarea, setzero(grid, row, col))
                    

        return maxarea
        