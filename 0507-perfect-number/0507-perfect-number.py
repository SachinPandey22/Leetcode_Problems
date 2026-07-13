class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 0
        if num == 1:
            return False
        for i in range(1, int(math.sqrt(num))+1, 1):
            if num % i == 0:
                sum = sum + i
                if i != num/i and num/i != num: 
                    sum = sum + num/i
        return num == sum
        