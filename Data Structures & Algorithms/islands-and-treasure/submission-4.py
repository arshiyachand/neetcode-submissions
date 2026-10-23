class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])

        queue = collections.deque([])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append([row,col,0])

        if not queue:
            return

        directions = [(1,0), (-1,0) ,(0,1),(0,-1)]

        while queue:
            cur_row, cur_col, distance = queue.popleft()

            for r , c in directions:
                nr = cur_row + r
                nc = cur_col + c
                if (0<= nr < rows) and (0<= nc < cols) and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = distance + 1
                    queue.append([nr, nc, distance + 1])


        