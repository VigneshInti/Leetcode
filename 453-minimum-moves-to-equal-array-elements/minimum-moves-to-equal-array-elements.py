class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        Calculate minimum number of moves to make all array elements equal.
      
        In each move, we can increment n-1 elements by 1.
        This is mathematically equivalent to decrementing 1 element by 1.
      
        The minimum number of moves equals the sum of differences between 
        each element and the minimum element.
      
        Formula: sum(nums) - min(nums) * len(nums)
      
        Args:
            nums: List of integers
          
        Returns:
            Minimum number of moves required
        """
        # Find the minimum value in the array
        min_value = min(nums)
      
        # Calculate total sum of all elements
        total_sum = sum(nums)
      
        # The number of moves equals the total difference from minimum
        # This is equivalent to: sum of (each element - min_value)
        return total_sum - min_value * len(nums)
