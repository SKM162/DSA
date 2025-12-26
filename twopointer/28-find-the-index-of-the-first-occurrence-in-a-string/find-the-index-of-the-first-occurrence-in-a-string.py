# find occurrence of substring
# "" empty is also an occurrence.
# sliding window - check for all possible starting points
# first char match and length of substring left in main array.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                if haystack[i: i + len(needle)] == needle:
                    return i
        return -1


                    

        