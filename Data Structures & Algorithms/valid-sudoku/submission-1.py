class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        sections = []
        

        for i in board:
            rows.append(set())
            cols.append(set())
            sections.append(set())

        for row in range(len(rows)):
            for col in range(len(cols)):
                section = (row // 3) + (col // 3) * 3
                num = board[row][col]
                if num != "." and (num in rows[row] or num in cols[col] or num in sections[section]):
                    return False
                rows[row].add(num)
                cols[col].add(num)
                sections[section].add(num)

        return True