#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
import collections
from typing import List

# @lc code=start


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        queue = collections.deque()
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        ans = 0

        while queue:
            x, y, step = queue.popleft()
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and (nx, ny) not in visited:
                    ans = max(ans, step + 1)
                    queue.append((nx, ny, step + 1))
                    visited.add((nx, ny))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    return -1

        return ans

# @lc code=end
