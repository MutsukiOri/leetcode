class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        temp = 0

        for k in s:
            while temp < len(t):
                if t[temp] == k:
                    break
                else:
                    temp += 1
            temp += 1
        print(temp)
        return temp <= len(t) or temp == 0


# 模範回答

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i, j = 0, 0
#         while i < len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
#         return i == len(s)

solution = Solution()
s = 'abc'
t = 'ahbgdc'
print(solution.isSubsequence(s, t))
