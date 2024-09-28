from collections import deque
from functools import lru_cache

class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        N = len(positions)
        positions.append([kx, ky])  # positions[0..N-1]: pawns, positions[N]: knight's initial position

        # Build dist[i][j], distances between positions[i] and positions[j]
        N_positions = N + 1
        dist = [[0] * N_positions for _ in range(N_positions)]

        board_size = 50
        moves = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]

        for i in range(N_positions):
            start_x, start_y = positions[i]
            visited = [[-1] * board_size for _ in range(board_size)]
            queue = deque()
            queue.append((start_x, start_y))
            visited[start_x][start_y] = 0
            targets = set()
            for j in range(N_positions):
                if j != i:
                    targets.add((positions[j][0], positions[j][1], j))

            while queue and targets:
                x, y = queue.popleft()
                curr_dist = visited[x][y]
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < board_size and 0 <= ny < board_size and visited[nx][ny] == -1:
                        visited[nx][ny] = curr_dist + 1
                        queue.append((nx, ny))
                        if (nx, ny, -1) in targets:
                            continue
                        for tx, ty, j in list(targets):
                            if nx == tx and ny == ty:
                                dist[i][j] = visited[nx][ny]
                                targets.remove((tx, ty, j))
                                break

        from functools import lru_cache

        @lru_cache(None)
        def dp(mask, pos_index, player):
            if mask == 0:
                return 0
            if player == 0:  # Alice's turn
                res = float('-inf')
                for p in range(N):
                    if mask & (1 << p):
                        d = dist[pos_index][p]
                        new_mask = mask & ~(1 << p)
                        total_moves = d + dp(new_mask, p, 1 - player)
                        res = max(res, total_moves)
                return res
            else:  # Bob's turn
                res = float('inf')
                for p in range(N):
                    if mask & (1 << p):
                        d = dist[pos_index][p]
                        new_mask = mask & ~(1 << p)
                        total_moves = d + dp(new_mask, p, 1 - player)
                        res = min(res, total_moves)
                return res

        initial_mask = (1 << N) - 1
        initial_pos_index = N  # Knight's initial position index
        return dp(initial_mask, initial_pos_index, 0)
