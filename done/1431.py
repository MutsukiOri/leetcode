class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        ans = [kid + extraCandies >= max_candies for i,
               kid in enumerate(candies)]
        return ans
