from typing import List


class Solution:
    # Time: O(n), Space: O(k) where k = number of distinct elements
    def mostFrequentElement(self, nums: List[int]) -> int:
        
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        max_ele = max(freq.values())
        return min (k for k, v in freq.items() if v == max_ele)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 2, 3, 3, 3], 3),       # clear winner
        ([4, 4, 5, 5, 6], 4),          # tie -> smallest
        ([10, 9, 7], 7),               # all appear once -> smallest
        ([5], 5),                      # single element
        ([-1, -1, 2, 2, 3], -1),       # negatives in a tie
        ([7, 7, 7, 7], 7),             # all same
        ([3, 1, 3, 1, 2, 2], 1),       # three-way tie, unsorted
    ]
    for nums, expected in tests:
        result = sol.mostFrequentElement(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: nums={nums} -> got {result}, expected {expected}")
