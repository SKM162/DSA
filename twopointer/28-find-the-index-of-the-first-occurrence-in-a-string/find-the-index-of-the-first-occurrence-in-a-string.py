# 28. Find the Index of the First Occurrence in a String - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=problem-list-v2&envId=two-pointers
# find substring in string
# two pointer - staged
# left finds the first char of substring
# right checks full occurrence.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)):
            # find match of first char
            if haystack[i] == needle[0]:
                j = 1
                while j < len(needle) and i + j < len(haystack) and needle[j] == haystack[i+j]:
                    j += 1
                if j == len(needle):
                    return i
        return -1
                    

        