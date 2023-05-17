class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                temp = ''
                while stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * temp)
            else:
                stack.append(char)
        return ''.join(stack)


solution = Solution()
s = "3[a2[c]]"
print(solution.decodeString(s))
