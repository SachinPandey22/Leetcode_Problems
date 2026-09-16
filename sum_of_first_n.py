class Solution:
    def sumOfFirstN(self, n: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (5, 15),
        (1, 1),
        (0, 0),
        (10, 55),
        (100, 5050),
    ]
    for n, expected in tests:
        result = sol.sumOfFirstN(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: n={n} -> got {result}, expected {expected}")
