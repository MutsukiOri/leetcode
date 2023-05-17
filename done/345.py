"""
Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u',
and they can appear in both lower and upper cases, more than once.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_reversed = []
        ans = []
        for i in range(len(s)):
            if s[i] in vowels:
                s_reversed.append(s[i])
        for k in range(len(s)):
            if s[k] in vowels:
                ans.append(s_reversed.pop())
            else:
                ans.append(s[k])
        return ''.join(ans)


solution = Solution()
s = input()
print(solution.reverseVowels(s))
