class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(substring):
            return substring == substring[::-1]

        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s[left:right]) or is_palindrome(s[left+1:right+1])
            left += 1
            right -=1
        return True
