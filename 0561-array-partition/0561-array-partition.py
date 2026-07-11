'''
   p   q   
[1,2,3,4] = 4 ->

(1,2) + (3,4) = 1 + 3
(1,3) + (2,4) = 1 + 2
(1,4) + (2,3) = 1 + 2

 p.    q
[1,2,3,4,5,6]

(1,2) (3,4) (5,6)

[1,2,2,5,6,6]
1 + 2 + 6 

Time complexity - O(nlogn)
Space complexity - O(1)

'''


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        i = 0
        summation = 0

        while i <len(nums):
            summation+=nums[i]
            i+=2
        
        return summation












            



        