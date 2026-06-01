"""
Time complexity - O(n)
Space complexity - O(n)

Intution

1. We need to run twice to find the maximum first run will be from index 0 to n-1
2. Second run will be from index 1 to n
3. Using the result of both the runs we need to find the maximum
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(subarray):
            if len(subarray) == 1:
                return subarray[0]
            total_loot = []
            total_loot.append(subarray[0])
            total_loot.append(max(subarray[0], subarray[1]))

            for i in range(2, len(subarray)):
                total_loot.append(
                    max(total_loot[i - 2] + subarray[i], total_loot[i - 1])
                )
            return total_loot[-1]

        run1 = helper(nums[0 : len(nums) - 1])
        run2 = helper(nums[1 : len(nums)])

        return max(run1, run2)
