#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#
import collections

# @lc code=start
class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        n, m = len(maze), len(maze[0])
        queue = collections.deque([(entrance[0], entrance[1], 0)])
        visited = set()
        visited.add((entrance[0], entrance[1]))
        while queue:
            x, y, step = queue.popleft()
            if (x, y) != (entrance[0], entrance[1]) and (x == 0 or x == n - 1 or y == 0 or y == m - 1):
                return step
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == "." and (nx, ny) not in visited:
                    queue.append((nx, ny, step + 1))
                    visited.add((nx, ny))
        return -1


# @lc code=end

solution = Solution()
maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]]
entrance = [0, 1]
print(solution.nearestExit(maze, entrance))
