
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Coordinate compression for Fenwick Tree.
        values = sorted(set(nums))
        m = len(values)

        def get_index(value):
            import bisect
            return bisect.bisect_left(values, value)

        # Fenwick Trees:
        # One stores frequencies, another stores sums.
        count_tree = [0] * (m + 1)
        sum_tree = [0] * (m + 1)

        def update(tree, index, delta):
            index += 1
            while index <= m:
                tree[index] += delta
                index += index & -index

        def query(tree, index):
            result = 0
            while index > 0:
                result += tree[index]
                index -= index & -index
            return result

        # Find the value at the given sorted position (1-based).
        def kth(kth_position):
            index = 0
            bit = 1 << (m.bit_length() - 1)

            while bit:
                nxt = index + bit

                if nxt <= m and count_tree[nxt] < kth_position:
                    index = nxt
                    kth_position -= count_tree[nxt]

                bit >>= 1

            return index

        # Calculate the minimum cost for every window of size x.
        costs = []
        window_sum = 0

        for i in range(n):
            value = nums[i]
            idx = get_index(value)

            # Add the new element.
            update(count_tree, idx, 1)
            update(sum_tree, idx, value)
            window_sum += value

            # Remove the element outside the window.
            if i >= x:
                old = nums[i - x]
                old_idx = get_index(old)

                update(count_tree, old_idx, -1)
                update(sum_tree, old_idx, -old)
                window_sum -= old

            # Calculate median cost when window is complete.
            if i >= x - 1:
                median_idx = kth((x + 1) // 2)
                median = values[median_idx]

                # Count and sum of elements <= median.
                left_count = query(count_tree, median_idx + 1)
                left_sum = query(sum_tree, median_idx + 1)

                right_count = x - left_count
                right_sum = window_sum - left_sum

                # Minimum operations to make the window equal.
                cost = (
                    median * left_count - left_sum
                    + right_sum - median * right_count
                )

                costs.append(cost)

        # DP: minimum cost to select exactly t non-overlapping windows.
        INF = float('inf')
        prev = [0] * (n + 1)

        for t in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):

                # Option 1: Do not select a window ending at i.
                curr[i] = curr[i - 1]

                # Option 2: Select the window [i-x, i).
                if i >= x:
                    start = i - x
                    candidate = prev[start] + costs[start]

                    curr[i] = min(curr[i], candidate)

            prev = curr

        return prev[n]
