'''
Complexity:
Time: O(n)
Space: O(n)
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        hashmap = {0: 1}

        for num in nums:
            prefix += num
            count += hashmap.get(prefix - k, 0)
            hashmap[prefix] = hashmap.get(prefix, 0) + 1

        return count
