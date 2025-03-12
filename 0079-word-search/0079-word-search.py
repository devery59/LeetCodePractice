dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])

        def in_range(x, y):
            if x < 0 or x >= M:
                return False
            elif y < 0 or y >= N:
                return False
            return True

        def has_word(x, y, index, visited):
            if not in_range(x, y):
                return False
            if word[index] != board[x][y]:
                return False
            if (x, y) in visited:
                return False
            if len(word[index:]) == 1:
                return True
            visited.add((x, y))
            for i in range(0, 4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if has_word(next_x, next_y, index + 1, visited):
                    return True

            visited.remove((x, y))
            return False

        for j in range(0, M):
            for k in range(0, N):
                if has_word(j, k, 0, set()):
                    return True
        return False