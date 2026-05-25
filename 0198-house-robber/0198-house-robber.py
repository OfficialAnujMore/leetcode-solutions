"""
Time complexity - O(n)
Space complexity - O(n)

Use dynamic programming where total_loot[i] stores the maximum amount
that can be robbed from houses 0 through i.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return nums[0]

        total_loot = []
        total_loot.append(nums[0])
        total_loot.append(max(nums[0], nums[1]))

        for i in range(2, n):
            total_loot.append(max(total_loot[i - 2] + nums[i], total_loot[i - 1]))

        return total_loot[-1]
