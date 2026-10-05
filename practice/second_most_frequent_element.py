from typing import List


class Solution:
    # Time: O(n), Space: O(k) where k = number of distinct elements
    def secondMostFrequentElement(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        max_val = max(dic.values())
        nd_max = -1
        for i in dic.values():
            if i < max_val and i > nd_max:
                nd_max = i
        if nd_max == -1:
            return -1
        return min(k for k, v in dic.items() if v == nd_max)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 2, 3, 3, 3], 2),               # clear second
        ([4, 4, 5, 5, 6], 6),                  # tie for first, single second
        ([10, 10, 10, 9, 9, 8, 8], 8),         # tie for second -> smallest
        ([3, 3, 3, 3, 1, 1, 2, 5], 1),         # second freq is 2, not 1
        ([-2, -2, -1, -1, -1, 0], -2),         # negatives
        ([1, 1, 2, 2, 3, 3], -1),              # all same freq -> no second
        ([5, 5, 5, 5], -1),                    # only one distinct element
        ([7], -1),                             # single element
    ]
    for nums, expected in tests:
        result = sol.secondMostFrequentElement(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: nums={nums} -> got {result}, expected {expected}")
