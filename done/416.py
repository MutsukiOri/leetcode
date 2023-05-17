class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)

        # if the total sum is odd, we can't partition into two equal subsets
        if total_sum % 2 != 0:
            return False

        # target sum of each subset is half of the total sum
        target = total_sum // 2

        # create a boolean table of size len(nums) x target
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]

        # base case: dp[i][0] is True for all i since an empty subset can always sum to zero
        for i in range(len(nums)):
            dp[i][0] = True

        # base case: dp[0][nums[0]] is True if nums[0] <= target
        if nums[0] <= target:
            dp[0][nums[0]] = True

        # fill the remaining table
        for i in range(1, len(nums)):
            for j in range(1, target + 1):
                if j < nums[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]

        return dp


solution = Solution()
nums = [1, 5, 5, 11]
print(solution.canPartition(nums))
