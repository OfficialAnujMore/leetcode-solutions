class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        freq = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in freq:
                return [i, freq[difference]]
            else:
                freq[num] = i
        return []
