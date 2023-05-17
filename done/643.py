class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        temp_max = sum(nums[:k])
        temp = sum(nums[:k])
        for i in range(len(nums) - k):
            print(temp_max, temp)
            temp = temp - nums[i] + nums[i + k]
            temp_max = max(temp_max, temp)

        return temp_max / k


solution = Solution()
print(solution.findMaxAverage([0, 4, 0, 3, 2], 1))
