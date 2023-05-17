class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        S = [0] * len(s)
        for i in range(len(S)):
            if s[i] in vowels:
                S[i] = 1

        return self.findMax(S, k)

    def findMax(self, nums: list[int], k: int) -> float:
        temp_max = sum(nums[:k])
        temp = sum(nums[:k])
        for i in range(len(nums) - k):
            print(temp_max, temp)
            temp = temp - nums[i] + nums[i + k]
            temp_max = max(temp_max, temp)

        return temp_max
