class Solution:
    def reverse(self, x: int) -> int:
        y = 0

        if x < 0:
            neg = -1
        else:
            neg = +1

        x = abs(x)
        while x > 0:
            last = x % 10
            y = y*10 + last
            x = x//10
        rev = y * neg
        if rev< -2**31 or rev>2**31 -1:
            return 0

        return rev
        
        