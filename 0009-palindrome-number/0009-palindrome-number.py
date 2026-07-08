class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        z = x
        last = 0
        if x < 0:
            return False
        if x == 0:
            return True
        while x > 0:
            last = x % 10
            y = y * 10 + last
            x = x // 10
        return z == y
