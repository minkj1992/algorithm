# https://leetcode.com/problems/max-area-of-island/
import collections
from typing import Generator, Tuple, List

LAND = 1
WATER = 0
MOVE = ((0, 1), (0, -1), (1, 0), (-1, 0))


def move(y: int, x: int):
    for dy, dx in MOVE:
        yield y + dy, x + dx


class Solution:
    def is_in_grid(self, y, x) -> bool:
        return (0 <= y < self.n) and (0 <= x < self.m)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        self.grid = grid
        self.visited = [[False] * self.m for _ in range(self.n)]

        max_area_size = 0
        for y in range(self.n):
            for x in range(self.m):
                if grid[y][x] == LAND and not self.visited[y][x]:
                    max_area_size = max(self.bfs(y, x), max_area_size)
        return max_area_size

    def bfs(self, start_y, start_x) -> int:
        area_size = 1
        self.visited[start_y][start_x] = True
        queue = collections.deque([(start_y, start_x)])

        while queue:
            y, x = queue.pop()
            for ny, nx in move(y, x):
                if not self.is_in_grid(ny, nx) or self.visited[ny][nx] or self.grid[ny][nx] == WATER:
                    continue

                area_size += 1
                self.visited[ny][nx] = True
                queue.appendleft((ny, nx))
        return area_size
