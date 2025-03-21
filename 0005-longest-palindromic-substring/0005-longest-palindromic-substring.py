class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        if len(s) == 1:
            return s
        for i in range(len(s)):
            for j in range(i + 1, len(s)+1):
                if self.is_palindrome(s[i:j]):
                    if len(s[i:j]) > len(answer):
                        answer = s[i:j]
        return answer

    def is_palindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        return False