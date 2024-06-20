class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Helper function to check if a block (row, column, or sub-box) is valid
        def is_valid_block(block):
            seen = set()
            for num in block:
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
            return True
        for row in board:
            if not is_valid_block(row):
                return False
        for col in range(9):
            if not is_valid_block([board[row][col] for row in range(9)]):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [
                    board[x][y]
                    for x in range(i, i + 3)
                    for y in range(j, j + 3)
                ]
                if not is_valid_block(sub_box):
                    return False
        
        return True

    def hasEmptyCells(self, board: List[List[str]]) -> bool:
        for row in board:
            if '.' in row:
                return True
        return False
