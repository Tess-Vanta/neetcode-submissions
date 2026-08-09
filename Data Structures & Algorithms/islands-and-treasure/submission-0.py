class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        WATER, TREASURE, LAND = -1, 0, 2147483647
        n, m = len(grid), len(grid[0])

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == TREASURE:
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == LAND:
                    grid[nx][ny] = grid[x][y] + 1
                    q.append((nx, ny))