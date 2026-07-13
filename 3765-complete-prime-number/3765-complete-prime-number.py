class Solution:
    def completePrime(self, num: int) -> bool:
        def isPrime(n:int) -> bool:
            if n == 1:
                return False
            for i in range(2, int(math.sqrt(n))+1, 1):
                if n % i == 0:
                    return False
            return True
        prefix = []
        suffix = []
        if num <= 9 and isPrime(num) == True:
            return True
        p = num
        while p > 0:
            prefix.append(p)
            p //= 10
        
        divisor = 10
        while divisor < num:
            suffix.append(num % divisor)
            divisor *= 10
        combined = prefix + suffix
        for i in combined:
            if isPrime(i) == False:
                return False
        return True