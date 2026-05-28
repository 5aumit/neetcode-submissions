class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen = set()

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue

                r = f'{board[i][j]} found in row {i}'
                c = f'{board[i][j]} found in col {j}'
                b = f'{board[i][j]} found in box {i//3},{j//3}'

                if r in seen:
                    return False
                else:
                    seen.add(r)

                if c in seen:
                    return False
                else:
                    seen.add(c)

                if b in seen:
                    return False
                else:
                    seen.add(b)

        return True