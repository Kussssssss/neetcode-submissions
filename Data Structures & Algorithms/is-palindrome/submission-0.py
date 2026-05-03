class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = "".join(char.lower() for char in s if char.isalnum())

        return formatted==formatted[::-1]