class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def calculate_digit_sum(number: int) -> int:
            """Calculate the sum of digits of a given number."""
            digit_sum = 0
            while number:
                digit_sum += number % 10
                number //= 10
            return digit_sum

        n = len(nums)
      
        # Create array of tuples (digit_sum, original_value) and sort by digit sum
        sorted_pairs = sorted((calculate_digit_sum(num), num) for num in nums)
      
        # Create a mapping from original value to its target position after sorting
        value_to_target_position = {pair[1]: index for index, pair in enumerate(sorted_pairs)}
      
        # Initialize answer as total elements (we'll subtract number of cycles)
        min_swaps_needed = n
        visited = [False] * n
      
        # Find all cycles in the permutation
        for i in range(n):
            if not visited[i]:
                # Found a new cycle, subtract 1 from answer (cycle of length k needs k-1 swaps)
                min_swaps_needed -= 1
                current_position = i
              
                # Traverse the entire cycle and mark all positions as visited
                while not visited[current_position]:
                    visited[current_position] = True
                    # Move to the target position of the current element
                    current_position = value_to_target_position[nums[current_position]]
      
        return min_swaps_needed

