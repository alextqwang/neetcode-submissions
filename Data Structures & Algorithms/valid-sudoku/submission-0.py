class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = [set() for _ in range(9)]
        colset = [set() for _ in range(9)]
        boxset = [set() for _ in range(9)]
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                box = (r // 3) * 3 + (c // 3)
                if col != ".":
                    if col in rowset[r] or col in colset[c] or col in boxset[box]:
                        return False
                    rowset[r].add(col)
                    colset[c].add(col)
                    boxset[box].add(col)
        return True
