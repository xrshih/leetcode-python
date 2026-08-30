class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            currstart = s[left]
            currlast = s[right]
            if not currstart.isalnum():
                left += 1
            elif not currlast.isalnum():
                right -= 1
            else:
                if currstart.lower() != currlast.lower():
                    return False
                left += 1
                right -= 1

        return True