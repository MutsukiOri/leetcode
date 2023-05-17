#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.maxStage = -10**6
        self.ans = 0

        def calcLevelSum(stage: list[TreeNode], level: int):
            n = len(stage)
            if n == 0:
                return
            cnt = 0
            for i in range(n):
                temp = stage.pop(0)
                cnt += temp.val
                if temp.left:
                    stage.append(temp.left)
                if temp.right:
                    stage.append(temp.right)
            if self.maxStage < cnt:
                self.maxStage = cnt
                self.ans = level
            calcLevelSum(stage, level + 1)
        
        calcLevelSum([root], 1)

        return self.ans


# @lc code=end
