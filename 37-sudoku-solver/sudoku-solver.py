
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty = []

        # Store existing numbers
        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    empty.append((r, c))

                else:
                    num = board[r][c]
                    b = (r // 3) * 3 + (c // 3)

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

        def backtrack(pos):

            if pos == len(empty):
                return True

            # Find the empty cell with fewest candidates
            best = pos
            min_options = 10

            for k in range(pos, len(empty)):
                r, c = empty[k]
                b = (r // 3) * 3 + (c // 3)

                available = 9 - len(
                    rows[r] | cols[c] | boxes[b]
                )

                if available < min_options:
                    min_options = available
                    best = k

                if available == 0:
                    return False

                if available == 1:
                    break

            # Swap the selected cell into current position
            empty[pos], empty[best] = empty[best], empty[pos]

            r, c = empty[pos]
            b = (r // 3) * 3 + (c // 3)

            used = rows[r] | cols[c] | boxes[b]

            for num in "123456789":

                if num not in used:

                    board[r][c] = num

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

                    if backtrack(pos + 1):
                        return True

                    # Undo the choice
                    board[r][c] = "."

                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[b].remove(num)

            # Restore empty-cell ordering
            empty[pos], empty[best] = empty[best], empty[pos]

            return False

        backtrack(0)
