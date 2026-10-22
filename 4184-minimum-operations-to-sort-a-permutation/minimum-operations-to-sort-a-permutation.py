from typing import List
from math import inf


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Total number of elements in the array.
        n = len(nums)

        # Find the index of the single zero in the array.
        zero_index = nums.index(0)

        def is_sorted_with_step(step: int) -> bool:
            """
            Check whether traversing the array starting from `zero_index`
            with the given circular `step` produces a non-decreasing sequence.

            Each position is computed modulo n to wrap around the array,
            simulating a circular traversal in either direction.
            """
            for i in range(1, n):
                # Previous position in the circular traversal.
                prev_pos = (zero_index + (i - 1) * step) % n
                # Current position in the circular traversal.
                curr_pos = (zero_index + i * step) % n

                # If order is violated, the step direction is invalid.
                if nums[prev_pos] > nums[curr_pos]:
                    return False

            return True

        # Track the minimum number of operations found so far.
        answer = inf

        # Case 1: traversal in the forward direction (step = +1).
        if is_sorted_with_step(1):
            # Option A: rotate so the zero moves to the front directly.
            answer = min(answer, zero_index)
            # Option B: account for the wrap-around cost.
            answer = min(answer, n - zero_index + 2)

        # Case 2: traversal in the backward direction (step = -1).
        if is_sorted_with_step(-1):
            # Option A: cost considering the offset from the front.
            answer = min(answer, zero_index + 2)
            # Option B: rotate so the zero aligns from the back.
            answer = min(answer, n - zero_index)

        # If no valid arrangement was found, return -1.
        return -1 if answer == inf else answer
