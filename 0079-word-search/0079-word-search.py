dx = [-1, 1, 0, 0]  # Up, down, left, right
dy = [0, 0, -1, 1]


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])

        def in_range(x, y):
            return 0 <= x < M and 0 <= y < N

        def has_word(x, y, index, visited):
            # Base case: if all characters are matched
            if index == len(word):
                return True

            # Check if current position is valid
            if not in_range(x, y) or (x, y) in visited or board[x][y] != word[index]:
                return False

            # Mark current cell as visited
            visited.add((x, y))

            # Explore all 4 directions
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if has_word(next_x, next_y, index + 1, visited):
                    return True

            # Backtrack: remove current cell from visited
            visited.remove((x, y))
            return False

        # Try starting from each cell
        for j in range(M):
            for k in range(N):
                if has_word(j, k, 0, set()):  # Start with empty visited set
                    return True
        return False
