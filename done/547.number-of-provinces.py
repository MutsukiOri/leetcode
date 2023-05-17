#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces_num = 0
        n = len(isConnected)
        not_checked = set(range(n))

        def dfs(i: int):
            not_checked.discard(i)
            for j in range(n):
                if isConnected[i][j] and j in not_checked:
                    dfs(j)

        while not_checked:
            provinces_num += 1
            check = not_checked.pop()
            dfs(check)
        
        return provinces_num


# @lc code=end
