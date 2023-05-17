#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        self.ans = []

        def right(stage: List[TreeNode]):
            n = len(stage)
            if n > 0:
                self.ans.append(stage[0].val)
                for k in range(n):
                    temp = stage.pop(0)
                    if temp.right:
                        stage.append(temp.right)
                    if temp.left:
                        stage.append(temp.left)

                right(stage)
            else:
                return

        right([root])
        return self.ans
# @lc code=end
