

def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []
    board = []

    def dfs(row):
        # We successfully placed all n queens
        if row == n:
            solutions.append(board.copy())
            return

        # Try every column in this row
        for col in range(n):

            # Check if this position is safe
            safe = True

            for prev_row in range(row):
                prev_col = board[prev_row]

                # Same column
                if prev_col == col:
                    safe = False
                    break

                # Same diagonal
                if abs(prev_col - col) == abs(prev_row - row):
                    safe = False
                    break

            if safe:
                # Place queen
                board.append(col)

                # DFS to next row
                dfs(row + 1)

                # Backtrack
                board.pop()

    dfs(0)

    return solutions