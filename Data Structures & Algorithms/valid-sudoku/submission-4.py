class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = dict(zip(
            [f'row{i}' for i in range(9)],
            [set() for _ in range(9)]
        ))

        cols = dict(zip(
            [f'col{i}' for i in range(9)],
            [set() for _ in range(9)]
        ))

        grids = {f"grid{i}{j}" : set() for i in range(3) for j in range(3)}

        # print(rows,cols,grids)

        for r in range(9):
            for c in range(9):

                num = board[r][c]

                if num == '.':
                    continue
                else:
                    num = int(num)

                if num in rows[f'row{r}']:
                    print(f'Failed at {r,c} for row {r}')
                    return False
                else:
                    rows[f'row{r}'].add(num)


                if num in cols[f'col{c}']:
                    print(f'Failed at {r,c} for col {c}')
                    return False
                else:
                    cols[f'col{c}'].add(num)


                if num in grids[f'grid{r//3}{c//3}']:
                    print(f'Failed at {r,c} for grid{r//3}{c//3}')
                    return False
                else:
                    grids[f'grid{r//3}{c//3}'].add(num)

        return True

