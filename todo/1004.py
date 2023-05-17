class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        right = 0
        max_len = 0
        zero_count = 0
        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len


solution = Solution()
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(solution.longestOnes(nums, k))

# give up
# 2023/05/03
# 1004.py
# written by copilot


# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         left = zeroCounter = 0
#         for right, num in enumerate(nums):
#             if num == 0:
#                 zeroCounter += 1
#             if zeroCounter > k:
#                 if nums[left] == 0: zeroCounter -= 1
#                 left += 1

#         return right - left + 1