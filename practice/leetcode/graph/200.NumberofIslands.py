# https://leetcode.com/problems/number-of-islands/
from collections import deque

MOVE = ((0, 1), (0, -1), (1, 0), (-1, 0))
LAND = "1"
WATER = "0"


def move(y, x):
    for dy, dx in MOVE:
        yield y + dy, x + dx


class Solution:
    def is_in_grid(self, y, x) -> bool:
        return (0 <= y < self.n) and (0 <= x < self.m)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        self.grid = grid
        self.visited = [[False] * self.m for _ in range(self.n)]

        num_island = 0
        for y in range(self.n):
            for x in range(self.m):
                if grid[y][x] == LAND and not self.visited[y][x]:
                    self.bfs(y, x)
                    num_island += 1
        return num_island

    def bfs(self, start_y, start_x):
        self.visited[start_y][start_x] = True
        queue = deque([(start_y, start_x)])

        while queue:
            y, x = queue.pop()
            for ny, nx in move(y, x):
                if not self.is_in_grid(ny, nx) or self.visited[ny][nx] or self.grid[ny][nx] == WATER:
                    continue

                self.visited[ny][nx] = True
                queue.appendleft((ny, nx))
