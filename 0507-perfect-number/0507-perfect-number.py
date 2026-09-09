class Solution:
    import math
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 0
        if num <= 1 or num > 10**8:
            return False
        for n in range(1, int(math.sqrt(num)) +1 , 1):
            if num%n ==0:
                sum += n
                if n!=num/n and num/n !=num:
                    sum += num/n
        return sum == num