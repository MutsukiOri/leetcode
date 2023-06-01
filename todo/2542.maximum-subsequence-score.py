#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#
from typing import List
import heapq

# @lc code=start


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key=lambda x: -x[1])

        top_k_heap = [x[0] for x in pairs[:k]]
        top_k_sum = sum(top_k_heap)
        heapq.heapify(top_k_heap)

        ans = top_k_sum * pairs[k - 1][1]

        for i in range(k, len(nums1)):
            top_k_sum -= heapq.heappop(top_k_heap)
            top_k_sum += pairs[i][0]
            heapq.heappush(top_k_heap, pairs[i][0])

            ans = max(ans, top_k_sum * pairs[i][1])

        return ans

# @lc code=end


solution = Solution()
print(solution.maxScore([1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12], 2))
# print(solution.get_subsequences([1, 1, 1, 1, 1, 1, 1, 1], 2))
# print(sum((1,1)))
