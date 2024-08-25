from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isvalid(board,row,col,m):
            for i in range(9):
                if str(board[row][i]) == m or str(board[i][col]) == m:
                    return False
            for h in range((row//3)*3,(row//3)*3+3):
                for k in range((col//3)*3,(col//3)*3+3):
                    if str(board[h][k]) == m:
                        return False
            return True
        def backtracing(board,i):
            if i == 81:
                return
            row,col = divmod(i,9)
            if board[row][col] != '.':
                backtracing(board,i+1)

            for m in range(1,10):
                if isvalid(board,row,col,str(m)):
                    board[row][col] = str(m)
                    backtracing(board,i+1)
                    board[row][col] = str(m)
        backtracing(board,0)
        return board
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
s = Solution()
print(s.solveSudoku(board))