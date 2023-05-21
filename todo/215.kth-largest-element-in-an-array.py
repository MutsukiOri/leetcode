#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
from typing import List

# @lc code=start


# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         return nums[-k]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapify(nums, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            # 左の子ノードが親ノードより大きい場合
            if left < n and nums[left] > nums[largest]:
                largest = left

            # 右の子ノードが親ノードまたは左の子ノードより大きい場合
            if right < n and nums[right] > nums[largest]:
                largest = right

            # 最大値が親ノードではない場合、要素を交換し再帰的に呼び出す
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, n, largest)

        # def heap_sort(nums):
        #     n = len(nums)

        #     # リストをヒープ構造に変換
        #     for i in range(n // 2 - 1, -1, -1):
        #         heapify(nums, n, i)

        #     # ヒープから要素を取り出し、ソートする
        #     for i in range(n - 1, 0, -1):
        #         nums[0], nums[i] = nums[i], nums[0]
        #         heapify(nums, i, 0)

        #     return nums
        n = len(nums)

        # リストをヒープ構造に変換
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)

        # ヒープから要素を取り出し、ソートする
        for i in range(n - 1, n - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(nums, i, 0)

        return nums[0]
        


# @lc code=end

solution = Solution()
print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
