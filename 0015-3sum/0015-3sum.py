"""
[-1,0,1,2,-1,-4]

[-4,-1,-1,0,1,2]

(-1,0,1) === 0

(-1,-1,2) === 0

[-6,-5,-4,-1,10,19]

"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []

        nums = sorted(nums)
        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            summation = 0

            while j < k:

                summation = nums[i] + nums[j] + nums[k]

                if summation == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif summation >= 0:
                    k -= 1
                else:
                    j += 1

        return result
