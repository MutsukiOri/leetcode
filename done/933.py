class RecentCounter:

    def __init__(self):
        self.requests = []
        return

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.pop(0)
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
solution = RecentCounter()
print(solution.ping(1))
print(solution.ping(100))
print(solution.ping(3001))
print(solution.ping(3002))
