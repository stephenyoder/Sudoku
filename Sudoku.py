from typing import List
import logging

class Sudoku:
    ans = []

    def __init__(self,):
        print("creating sudoku object")

    def validRow(self, board: List[List[int]], col) -> bool:
        # initialize set
        x = set()

        for i in range(8):
            if board[col][i] == 0:
                continue
            else:
                if board[col][i] in x:
                    return False
                else:
                    x.add(board[col][i])
        return True

    def validCol(self, board: List[List[int]], row) -> bool:
        x = set()

        for i in range(8):
            if board[i][row] == 0:
                continue
            else:
                if board[i][row] in x:
                    return False
                else:
                    x.add(board[i][row])
        return True

    def validGrid(self, board: List[List[int]]) -> bool:
        z = set()
        startX = 0
        startY = 0

        for chingamos in range(8):
            for i in range(2):
                for j in range(2):
                    if board[i + startX][j + startY] == 0:
                        continue
                    else:
                        if board[i + startX][j + startY] in z:
                            return False
                        else:
                            z.add(board[i + startX][j + startY])
            z.clear()
            if startX == 6:
                startX = 0
                startY += 3
            else:
                startX += 3

        return True

    def isValidSudoku(self, board: List[List[int]]) -> bool:
        for i in range(8):
            if not self.validGrid(board):
                return False
            else:
                if not self.validRow(board, i) or not self.validCol(board, i):
                    return False
            return True

    def checkElement(self, board: List[List[int]], col, row, val) -> bool:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        col_offset = col // 3 * 3
        row_offset = row // 3 * 3
        for j in range(3):
            for k in range(3):
                if val == board[row_offset+j][col_offset+k]:
                    return False

        for i in range(9):
            if val == board[row][i] or val == board[i][col]:
                return False

        return True

    def print_sudoku(self, board: List[List[int]]):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=" ")
                if j==2 or j==5: print("|", end=" ")
            print()
            if i==2 or i==5: print("-"*21)

        print()
        return

    def solve(self, board: List[List[int]]):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for val in range(1, 10):
                        if self.checkElement(board, col, row, val) is True:
                            board[row][col] = val
                            self.solve(board)
                            board[row][col] = 0
                    return
        self.ans.append(board)
        self.print_sudoku(board)
        return

if __name__ == '__main__':
    sudoku = Sudoku()
