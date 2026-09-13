class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for num in row:
                if num not in seen:
                    if num != ".":
                        seen.add(num)
                else:
                    return False
        
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen:
                    return False
                else:
                    if board[j][i] != ".":
                        seen.add(board[j][i])
        
        for i in range(0,9,3):
            for l in range(0,9,3):
                seen = set()
                for j in range(i, i+3):
                    for k in range(l, l+3):
                        if board[j][k] in seen:
                            return False
                        else:
                            if board[j][k] != ".":
                                seen.add(board[j][k])
        return True


