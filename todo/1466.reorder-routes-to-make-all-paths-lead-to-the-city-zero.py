#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.cnt = 0
        connected = [[] for _ in range(n)]
        for connection in connections:
            connected[connection[0]].append([connection[1], 1])
            connected[connection[1]].append([connection[0], -1])

        def dfs(node, parent):
            for child, sign in connected[node]:
                if child != parent:
                    if sign == 1:
                        self.cnt += sign
                    dfs(child, node)

        dfs(0, -1)
        return self.cnt






# @lc code=end
