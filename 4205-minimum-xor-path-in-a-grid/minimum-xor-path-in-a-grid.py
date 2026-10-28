from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Store all possible XOR values at each cell using a bitmask.
        dp = [[0] * n for _ in range(m)]

        # Initialize the starting cell.
        dp[0][0] = 1 << grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                reachable = 0

                # Get possible XOR values from above and left.
                if i > 0:
                    reachable |= dp[i - 1][j]
                if j > 0:
                    reachable |= dp[i][j - 1]

                value = grid[i][j]
                mask = 0

                # Update XOR values by including the current cell.
                for x in range(1024):
                    if reachable & (1 << x):
                        mask |= 1 << (x ^ value)

                dp[i][j] = mask

        # Return the minimum reachable XOR at the destination.
        for x in range(1024):
            if dp[m - 1][n - 1] & (1 << x):
                return x

        return 0