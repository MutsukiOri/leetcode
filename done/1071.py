class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # check if str1 and str2 are equal
        if str1 == str2:
            return str1

        # find the smaller string
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        # check if str2 divides str1
        if str1[:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)

        # no common divisor found
        return ""
