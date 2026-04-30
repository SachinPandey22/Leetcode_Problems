class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set(s)
        digit = []
        for n in nums:
            if n.isdigit():
                digit.append(int(n))
        if not digit or len(digit)==1:
            return -1
        largest = float('-inf')
        second_largest = float('-inf')

        for nu in digit:
            if nu > largest:
                second_largest = largest
                largest = nu
            elif nu > second_largest and nu != largest:
                second_largest = nu
        return second_largest

        