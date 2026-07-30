class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row = {}
            for j in range(9):
                if board[i][j] in row:
                    return False
                elif board[i][j] != '.':
                    row[board[i][j]] = 1

        for i in range(9):
            col = {}
            for j in range(9):
                if board[j][i] in col:
                    return False
                elif board[j][i] != '.':
                    col[board[j][i]] = 1

        top_corner = [0,0]
        for k in range(9):
            box = {}
            for i in range(3):
                for j in range(3):
                    if board[top_corner[0]+i][top_corner[1]+j] in box:
                        return False
                    elif board[top_corner[0]+i][top_corner[1]+j] != '.':
                        box[board[top_corner[0]+i][top_corner[1]+j]] = 1

            if (k+1) % 3 == 0:
                top_corner = [top_corner[0]+3, 0]
            else:
                top_corner = [top_corner[0], top_corner[1]+3]
        return True

        

        

        