"""
Bucket sort concept

Time complexity: O(n)
Space complexity: O(n)

Same intution as 451. Sort characters by frequencey
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        result = []

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        max_freq = -1
        freq_to_nums = {}

        for num, count in num_count.items():
            max_freq = max(max_freq, count)
            if count not in freq_to_nums:
                freq_to_nums[count] = [num]
            else:
                freq_to_nums[count].append(num)

        for freq in range(max_freq, 0, -1):
            if freq in freq_to_nums:
                nums_at_freq = freq_to_nums[freq]
                for num in nums_at_freq:
                    if k > 0:
                        result.append(num)
                        k -= 1

        return result
