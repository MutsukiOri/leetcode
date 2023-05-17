'''
Given an integer array nums,
return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.
'''


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False
        else:
            first = nums[0]
            second = None
            for i in range(1, len(nums)):
                if second is None:
                    if nums[i] > first:
                        second = nums[i]
                    else:
                        first = nums[i]
                else:
                    if nums[i] > second:
                        return True
                    elif nums[i] > first:
                        second = nums[i]
                    else:
                        first = nums[i]
            return False


solution = Solution()
nums = [19, 2, 9, 4, 1]
print(solution.increasingTriplet(nums))
