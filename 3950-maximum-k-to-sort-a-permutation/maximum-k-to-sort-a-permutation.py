from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # Initialize result with -1 (all bits set to 1 in two's complement)
        ans = -1

        # Iterate through the array with indices
        for i, x in enumerate(nums):
            # Check if element is not at its "sorted" position
            # (assuming 0-indexed positions should match values)
            if i != x:
                # Perform bitwise AND with misplaced elements
                # This keeps only common set bits across all misplaced values
                ans &= x

        # Return the result, ensuring non-negative output
        # If no misplaced elements found, ans remains -1, so return 0
        return max(ans, 0)
