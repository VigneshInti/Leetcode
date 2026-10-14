
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""

        result = []

        for i in range(num):
            digit = min(9, sum)
            result.append(str(digit))
            sum -= digit

        return "".join(result)
