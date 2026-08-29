class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for x in range(n-m+1):
            if haystack[x:x+m] == needle:
                return x
        return -1