class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for k in range(n - 1, -1, -1):
            if nums[k] == 0:
                nums.append(nums.pop(k))

# 反省
# Memoryの使用量が多い

# 以下, 省メモリの参考コード

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         z_count: int = 0

#         i = 0
#         while(i < len(nums)):

#             if(nums[i] == 0):
#                 z_count += 1
#                 nums.pop(i)

#             else:
#                 i += 1

#         for i in range(z_count):
#             nums.append(0)

#         return nums

# 0を見つけ次第pop,
# 0の数を数えておいて最後にまとめてappend
