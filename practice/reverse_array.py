from typing import List


class Solution:
    # Time: O(n), Space: O(1)
    def reverseArray(self, arr: List[int]) -> List[int]:
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([1], [1]),
        ([], []),
        ([7, 7, 7], [7, 7, 7]),
    ]
    for arr, expected in tests:
        original = list(arr)
        result = sol.reverseArray(arr)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: arr={original} -> got {result}, expected {expected}")
