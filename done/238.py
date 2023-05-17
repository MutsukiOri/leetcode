"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if len(nums) == 2:
            return [nums[1], nums[0]]
        if len(nums) == 3:
            return [nums[1] * nums[2], nums[0] * nums[2], nums[0] * nums[1]]
        if len(nums) > 3:
            return self.lib(nums)[0]

    def lib(self, nums: list[int]) -> tuple[list[int], int]:
        if len(nums) == 3:
            return ([nums[1] * nums[2], nums[0] * nums[2], nums[0] * nums[1]], nums[0] * nums[1] * nums[2])
        if len(nums) > 3:
            temp, total = self.lib(nums[:-1])
            temp = [i * nums[-1] for i in temp]
            temp.append(total)
            total *= nums[-1]
            return temp, total


solution = Solution()
nums = [1, 2, 3, 4]
print(solution.productExceptSelf(nums))
