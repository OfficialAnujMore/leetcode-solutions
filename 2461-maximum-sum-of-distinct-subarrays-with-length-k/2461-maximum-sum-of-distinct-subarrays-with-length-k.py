class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        result = 0
        hashmap = {}
        summation = 0

        for right in range(len(nums)):
            element = nums[right]
            summation += element
            hashmap[element] = hashmap.get(element, 0) + 1

            while hashmap[element] > 1:
                summation -= nums[left]
                hashmap[nums[left]] -= 1
                if hashmap[nums[left]] == 0:
                    del hashmap[nums[left]]
                left += 1

            if right - left + 1 == k:
                result = max(result, summation)
                summation -= nums[left]
                hashmap[nums[left]] -= 1
                if hashmap[nums[left]] == 0:
                    del hashmap[nums[left]]
                left += 1
        return result
