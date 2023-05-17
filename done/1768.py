class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        for i in range(min(len(word1), len(word2))):
            merged += word1[i] + word2[i]
        merged += word1[i + 1:] + word2[i + 1:]
        return merged
# solution = Solution()
# word1 = input()
# word2 = input()
# print(solution.mergeAlternately(word1, word2))
