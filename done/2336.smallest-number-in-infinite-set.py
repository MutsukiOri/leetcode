#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#

# @lc code=start
class SmallestInfiniteSet:

    def __init__(self):
        self.popedSet = set()
        self.smallest = 1

    def popSmallest(self) -> int:
        self.popedSet.add(self.smallest)
        ans = self.smallest
        while self.smallest in self.popedSet:
            self.smallest += 1
        return ans

    def addBack(self, num: int) -> None:
        if num in self.popedSet:
            self.popedSet.remove(num)
            if num < self.smallest:
                self.smallest = num
        return None


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end
