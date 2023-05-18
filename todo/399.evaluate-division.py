#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build graph
        graph = {}
        for i in range(len(equations)):
            if equations[i][0] not in graph:
                graph[equations[i][0]] = {}
            graph[equations[i][0]][equations[i][1]] = values[i]
            if equations[i][1] not in graph:
                graph[equations[i][1]] = {}
            graph[equations[i][1]][equations[i][0]] = 1 / values[i]

        # dfs
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if end in graph[start]:
                return graph[start][end]
            for node in graph[start]:
                if node not in visited:
                    visited.add(node)
                    tmp = dfs(node, end, visited)
                    if tmp != -1.0:
                        return graph[start][node] * tmp
            return -1.0

        # main
        res = []
        for query in queries:
            res.append(dfs(query[0], query[1], set()))
        return res



# @lc code=end

