class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        for i, num in enumerate(nums):
            if left == (total - num) / 2:
                return i
            else:
                left += num
        return -1


solution = Solution()
nums = [1, 7, 3, 6, 5, 6]
print(solution.pivotIndex(nums))
