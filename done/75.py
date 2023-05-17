class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        ans = 0
        border = 0
        while i < j:
            temp = min(height[i], height[j])
            border = max(border, temp)
            ans = max(ans, (j - i) * temp)
            if height[i] < height[j]:
                i += 1
                while height[i] < border and i < j:
                    i += 1
            else:
                j -= 1
                while height[j] < border and i < j:
                    j -= 1
        return ans


solution = Solution()
height = [1, 1]
print(solution.maxArea(height))
