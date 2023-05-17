import collections


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        cor = collections.Counter(arr)
        freq = collections.Counter(list(cor.values()))
        print(list(freq.keys()))
        return len(list(freq.keys())) >= len(list(cor.keys()))


solution = Solution()
arr = [1, 2, 2, 1, 1, 3]
print(solution.uniqueOccurrences(arr))
