"""
Time complexity - O(n)
Space complexity - O(1)

Intution
    At every index you need to track two things simultaneously:

    1. The maximum product ending at this position
    2. The minimum product ending at this position (because a very negative number can flip to a very large positive)

    When you land on a new number, three things could be your new max:

    1. The number itself (start fresh)
    2. Previous max * current number
    3. Previous min * current number (negative * negative = positive)

"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        curr_min = nums[0]
        curr_max = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            candidates = (n, curr_max * n, curr_min * n)

            curr_max = max(candidates)
            curr_min = min(candidates)
            result = max(result, curr_max)

        return result


"""
Dry Run - [2, 3, -2, 4, 4, -2]:
    | i     | n  | candidates (n, max*n, min*n) | curr_max | curr_min | result |
    |-------|----|------------------------------|----------|----------|--------|
    | start |    |                              | 2        | 2        | 2      |
    | 1     | 3  | (3, 6, 6)                    | 6        | 3        | 6      |
    | 2     | -2 | (-2, -12, -6)                | -2       | -12      | 6      |
    | 3     | 4  | (4, -8, -48)                 | 4        | -48      | 6      |
    | 4     | 4  | (4, 16, -192)                | 16       | -192     | 16     |
    | 5     | -2 | (-2, -32, 384)               | 384      | -32      | 384    |
"""
