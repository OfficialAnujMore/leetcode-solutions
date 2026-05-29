class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        prevTwo, prevOne = 1, 2

        for i in range(3, n + 1):
            curr = prevTwo + prevOne
            prevTwo = prevOne
            prevOne = curr

        return prevOne
