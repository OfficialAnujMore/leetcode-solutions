"""

Complexity:

Time: O(n)
Space: O(k)

"""


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        hashmap = {0: 1}

        for num in nums:
            prefix += num
            remainder = prefix % k
            count += hashmap.get(remainder, 0)
            hashmap[remainder] = hashmap.get(remainder, 0) + 1

        return count
