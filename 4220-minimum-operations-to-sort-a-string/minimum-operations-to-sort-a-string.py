from itertools import pairwise


class Solution:
    def minOperations(self, s: str) -> int:
        # Already non-decreasing: every char is <= the one after it.
        if all(prev <= curr for prev, curr in pairwise(s)):
            return 0

        # A length-2 string that isn't sorted is treated as impossible.
        if len(s) == 2:
            return -1

        # Smallest and largest characters in the string.
        min_char, max_char = min(s), max(s)

        # If the first char is the min (it's already in its ideal position)
        # or the last char is the max, a single operation is enough.
        if s[0] == min_char or s[-1] == max_char:
            return 1

        # If any interior character is the min or the max,
        # two operations are sufficient.
        if any(char in (min_char, max_char) for char in s[1:-1]):
            return 2

        # Otherwise, three operations are required.
        return 3
