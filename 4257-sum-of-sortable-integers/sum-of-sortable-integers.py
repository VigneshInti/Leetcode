
from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        answer = 0

        def is_rotation(block, target):
            k = len(block)

            # Build the KMP prefix table for target.
            pi = [0] * k
            j = 0

            for i in range(1, k):
                while j > 0 and target[i] != target[j]:
                    j = pi[j - 1]

                if target[i] == target[j]:
                    j += 1

                pi[i] = j

            # Search target in block + block, without
            # checking the duplicate final starting position.
            j = 0

            for i in range(2 * k - 1):
                value = block[i % k]

                while j > 0 and value != target[j]:
                    j = pi[j - 1]

                if value == target[j]:
                    j += 1

                if j == k:
                    return True

            return False

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for i in range(0, n, k):
                block = nums[i:i + k]
                target = s[i:i + k]

                if not is_rotation(block, target):
                    valid = False
                    break

            if valid:
                answer += k

        return answer
