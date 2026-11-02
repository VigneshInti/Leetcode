class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        """
        Find minimum number of moves to make all array elements equal.
        Each move consists of incrementing or decrementing an element by 1.
      
        The optimal strategy is to change all elements to the median value,
        as the median minimizes the sum of absolute deviations.
      
        Args:
            nums: List of integers
          
        Returns:
            Minimum total number of moves required
        """
        # Sort the array to find the median
        nums.sort()
      
        # Find the median element (middle element for odd length, 
        # or either middle element for even length)
        # Using bit shift (>> 1) is equivalent to integer division by 2
        median = nums[len(nums) >> 1]
      
        # Calculate total moves as sum of absolute differences from median
        # Each absolute difference represents the number of moves for that element
        total_moves = sum(abs(num - median) for num in nums)
      
        return total_moves
