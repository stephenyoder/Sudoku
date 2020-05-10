import unittest
from Sudoku import Sudoku

medium = [
[7,6,0,0,0,0,0,0,0],
[0,1,0,0,6,2,0,0,0],
[0,0,8,0,0,4,0,0,0],
[5,0,0,8,2,7,0,0,0],
[0,3,1,0,0,9,2,0,0],
[0,0,2,5,3,0,9,0,0],
[0,5,0,0,9,0,8,0,0],
[0,0,0,0,0,0,7,0,5],
[2,0,4,7,0,0,1,9,6]]

hard = [
[0,7,0,0,0,5,2,0,0],
[0,0,0,0,3,0,0,9,5],
[0,0,0,2,0,9,0,0,0],
[0,0,9,0,0,0,0,0,4],
[0,5,0,0,0,0,0,0,0],
[0,8,0,3,4,0,0,1,0],
[0,0,0,9,0,6,1,7,0],
[0,2,7,8,5,1,0,0,0],
[1,0,0,0,0,0,0,0,0]]

expert = [
[0,0,4,0,0,1,0,7,6],
[0,0,0,0,0,9,1,0,0],
[0,0,0,8,0,0,0,0,5],
[0,3,0,0,0,0,0,0,1],
[7,4,0,2,0,0,0,0,0],
[1,9,0,0,0,3,4,0,0],
[0,0,0,0,0,0,3,0,0],
[0,0,0,3,0,4,0,2,0],
[0,0,8,0,6,0,0,0,0]]

easy = [
    [6, 9, 0, 4, 0, 5, 0, 7, 0],
    [0, 0, 4, 9, 0, 0, 0, 0, 1],
    [8, 0, 5, 7, 6, 0, 4, 2, 9],
    [0, 4, 6, 1, 0, 0, 0, 3, 2],
    [0, 0, 0, 0, 9, 0, 0, 0, 5],
    [5, 0, 3, 2, 8, 4, 0, 0, 6],
    [3, 5, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 3, 0, 2, 5, 0],
    [2, 8, 0, 0, 0, 0, 6, 0, 0]]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sudoku = Sudoku()

        # solve the four sudoku puzzles
        sudoku.solve(easy)
        sudoku.solve(medium)
        sudoku.solve(hard)
        sudoku.solve(expert)

        # verify there are 4 solutions (1 for each puzzle)
        self.assertEqual(len(sudoku.ans), 4)

        for solution in sudoku.ans:
            # verify each sudoku solution is valid
            self.assertTrue(sudoku.isValidSudoku(solution))

if __name__ == '__main__':
    unittest.main()



