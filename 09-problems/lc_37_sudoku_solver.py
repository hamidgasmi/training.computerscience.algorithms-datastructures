"""
    1. Problem Summary / Clarifications / TDD:

    2. Intuition:
        - Backtracking.
        - Store filled values in 3 dictionaries of sets: rows, columns, boxes.
        - box_no = 3 * (r // 3) + c // 3
        - To go to next cells, use cell_no:
            - next cell: curr cell no + 1
            - col = cell_no % 9
            - row = cell_no // 9
            ---------------------------------------
            | 0   1   2 |  3   4   5 |  6   7   8 |
            | 9  10  11 | 12  13  14 | 15  16  17 |
            |18  19  20 | 21  22  23 | 24  25  26 |
            |-----------|------------|------------|
            |27  28  29 | 30  31  32 | 33  34  35 |
            |36  37  38 | 39  40  41 | 42  43  44 |
            |45  46  47 | 48  49  50 | 51  52  53 |
            |-----------|------------|------------|
            |54  55  56 | 57  58  59 | 60  61  62 |
            |63  64  65 | 66  67  68 | 69  70  71 |
            |72  73  74 | 75  76  77 | 78  79  90 |
            ---------------------------------------
    
    3. Complexity Analysis:
        - Time Complexity: O(9! * 8! * 7! * 6! * 5! * 4! * 3! * 2! * 1!) = O((9!)^9) = O(1)
        - Space Complexity: O(81) = O(1)
    
"""

class Solution:
    
    def __init__(self):
        self.size = 9
        self.cells_count = self.size**2

        self.values = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        self.empty = '.'

        self.box_no = lambda r, c: 3 * (r // 3) + c // 3   # Get box_no from row and column
        self.col_no = lambda cell_no: cell_no % self.size  # Get col no from cell. no
        self.row_no = lambda cell_no: cell_no // self.size # Get row no from cell. no

        self.rows_values = {} # {row: sudoku values set}
        self.cols_values = {} # {col: sudoku values set}
        self.boxs_values = {} # {box: sudoku values set}

    def solve_sudoku(self, board: List[List[str]]) -> None:

        # 1. Initialization: Store all board values in 3 dictionaries of sets: rows, columns and boxes
        for i in range(self.size):
            self.rows_values[i] = set()
            self.cols_values[i] = set()
            self.boxs_values[i] = set()
        
        for r in range(self.size):
            for c in range(self.size):
                if board[r][c] != self.empty:
                    self.rows_values[r].add(board[r][c])
                    self.cols_values[c].add(board[r][c])
                    self.boxs_values[self.box_no(r, c)].add(board[r][c])

        # 2. Backtrack from cell no: 0
        self.backtrack(0, board)

        return board

    def backtrack(self, cell_no, board):
        # Base case: we filled all empty cells
        if cell_no == self.cells_count: 
            return True

        r, c = self.row_no(cell_no), self.col_no(cell_no)

        if board[r][c] != self.empty:
            return self.backtrack(cell_no + 1, board)

        for val in self.values:
            # could_place? Is valid?
            if val in self.rows_values[r] or val in self.cols_values[c] or val in self.boxs_values[self.box_no(r, c)]:
                continue

            # place:
            board[r][c] = val
            self.rows_values[r].add(val)
            self.cols_values[c].add(val)
            self.boxs_values[self.box_no(r, c)].add(val)

            # next:
            if self.backtrack(cell_no + 1, board):
                return True

            # remove:
            board[r][c] = self.empty
            self.rows_values[r].remove(val)
            self.cols_values[c].remove(val)
            self.boxs_values[self.box_no(r, c)].remove(val)

        return False
        