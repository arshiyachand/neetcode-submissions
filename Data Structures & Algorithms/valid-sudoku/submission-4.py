class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsdict = defaultdict(set)
        colsdict = defaultdict(set)
        squaredict = defaultdict(set)


        for rows in range(9):
            for cols in range(9):
                if board[rows][cols] == ".":
                    continue
                if (board[rows][cols] in rowsdict[rows] or board[rows][cols] in colsdict[cols] or board[rows][cols] in squaredict[rows//3, cols//3]):
                    return False
                rowsdict[rows].add(board[rows][cols])
                colsdict[cols].add(board[rows][cols])
                squaredict[(rows//3,cols//3)].add(board[rows][cols]) 
        return True




        