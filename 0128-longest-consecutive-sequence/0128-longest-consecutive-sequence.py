"""
Time complexity - O(n)
Space complexity - O(n)

Intution:
1. First create a hashmap and mark every element as False
2. Loop through the nums array and mark the current element as true as it is visited and traverse in forward and reverse sequence to check if the number exists in sequence
3. While doing so check the current length and compare it with maximum to get the results
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        longest = 0
        for num in nums:
            hashmap[num] = False

        for num in nums:
            if hashmap[num]:
                continue
            hashmap[num] = True
            current_length = 1

            nextNum = num + 1
            while nextNum in hashmap and not hashmap[nextNum]:
                current_length += 1
                hashmap[nextNum] = True
                nextNum += 1

            prevNum = num - 1
            while prevNum in hashmap and not hashmap[prevNum]:
                current_length += 1
                hashmap[prevNum] = True
                prevNum -= 1

            longest = max(longest, current_length)

        return longest
