class Solution:
    # Time: O(x), Space: O(x) — recursion stack depth
    def factorial(self, x: int) -> int:
        if x == 0:
            return 1
        return x * self.factorial(x - 1)
        


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (0, 1),
        (1, 1),
        (5, 120),
        (10, 3628800),
        (20, 2432902008176640000),
    ]
    for x, expected in tests:
        result = sol.factorial(x)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: x={x} -> got {result}, expected {expected}")
