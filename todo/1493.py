# class Solution:
#     def longestSubarray(self, nums: list[int]) -> int:
#         left = 0
#         right = 0
#         max_len = 0
#         pop_count = 1
#         while right < len(nums):
#             if nums[right] == 0:
#                 pop_count -= 1
#             while pop_count < 0:
#                 if nums[left] == 0:
#                     pop_count += 1
#                 left += 1
#             max_len = max(max_len, right - left)
#             right += 1
#         return max_len


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        popCounter = 1
        for right, num in enumerate(nums):
            if num == 0:
                popCounter -= 1
            if popCounter < 0:
                if nums[left] == 0:
                    popCounter += 1
                left += 1
            print(left, right, popCounter)
        return right - left


solution = Solution()
nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
print(solution.longestSubarray(nums))
