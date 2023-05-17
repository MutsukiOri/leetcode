class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        if n == 1:
            return len(chars)
        else:
            if chars[-1] == chars[-2]:
                chars[-1] = 1
            for i in range(n - 2, 0, -1):
                if chars[i] == chars[i - 1] and type(chars[i + 1]) == int:
                    chars[i] = chars[i + 1] + 1
                    chars.pop(i + 1)
                elif chars[i] == chars[i - 1] and type(chars[i + 1]) == str:
                    chars[i] = 1
                elif chars[i] != chars[i - 1] and type(chars[i + 1]) == int:
                    chars[i + 1] += 1
                    chars[i + 1:i + 1] = ''.join(str(chars.pop(i + 1)))
                # elif chars[i] != chars[i - 1] and type(chars[i + 1]) == str:
            if type(chars[1]) == int:
                chars[1] += 1
                chars[1:1] = ''.join(str(chars.pop(1)))
            return len(chars)


solution = Solution()
chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(solution.compress(chars))
