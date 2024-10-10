class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                n = board[r][c]

                box_index = (r//3) * 3 + (c//3)
                if n in row_set[r] or n in col_set[c] or n in box_set[box_index]:
                    return False
                row_set[r].add(n)
                col_set[c].add(n)
                box_set[box_index].add(n)
        return True
    
    # https://leetcode.com/problems/valid-sudoku/