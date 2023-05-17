import collections

# 54'52"
# class Solution:
#     def equalPairs(self, grid: list[list[int]]) -> int:
#         grid_t = [list(x) for x in zip(*grid)]
#         grid = [','.join(map(str, i)) for i in grid]
#         grid_t = [','.join(map(str, i)) for i in grid_t]
#         set_grid = collections.Counter(grid)
#         set_grid_t = collections.Counter(grid_t)
#         grid_ans = set_grid & set_grid_t
#         ans = 0
#         for i in grid_ans.keys():
#             ans += set_grid[i] * set_grid_t[i]
#         return ans


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        grid_hash = [hash(tuple(grid[i])) for i in range(n)]
        counter1 = collections.Counter(grid_hash)

        grid_T = [[grid[j][i] for j in range(n)] for i in range(n)]
        grid_T_hash = [hash(tuple(grid_T[i])) for i in range(n)]
        counter2 = collections.Counter(grid_T_hash)
        print(grid_hash)
        print(counter1)

        res = 0
        for row in counter1.keys():
            if row in counter2.keys():
                res += counter1[row] * counter2[row]
        return res


solution = Solution()
grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
print(solution.equalPairs(grid))
