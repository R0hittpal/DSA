class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        ans = []
        board = [["."] * n for _ in range(n)]

        def is_safe(row, col):

            # Check same column
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Check upper-left diagonal
            r, c = row - 1, col - 1

            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False

                r -= 1
                c -= 1

            # Check upper-right diagonal
            r, c = row - 1, col + 1

            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False

                r -= 1
                c += 1

            return True

        def backtrack(row):

            # All rows completed
            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):

                if is_safe(row, col):

                    # Choose
                    board[row][col] = "Q"

                    # Explore
                    backtrack(row + 1)

                    # Undo
                    board[row][col] = "."

        backtrack(0)

        return ans