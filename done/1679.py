class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = 0
        while i < j:
            temp = nums[i] + nums[j]
            if temp < k:
                i += 1
            elif temp > k:
                j -= 1
            else:
                i += 1
                j -= 1
                ans += 1
        return ans


solution = Solution()
print(solution.maxOperations([1, 2, 3, 4], 5))
