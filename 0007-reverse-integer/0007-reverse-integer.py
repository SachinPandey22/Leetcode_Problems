class Solution:
    # x = 123, y =3, x = 12, 32, 1, 1, 321, 0
    def reverse(self, x: int) -> int:
        y = 0
        if x< -2 ** 31 or x> 2**31 -1:
            return 0
        if x <0:
            sign = -1
        else:
            sign = +1
        x = abs(x)
        while x > 0:
            y = y*10 + x%10
            x = x//10
        y = y * sign
        if y < -2**31 or y > 2**31 - 1:
            return 0
        return y
