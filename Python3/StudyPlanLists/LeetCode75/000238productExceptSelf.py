# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

from math import prod

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = list()
        for i in range(len(nums)):
            product = 1
            if i==0:
                product = product*prod(nums[i+1:])
            elif i == len(nums)-1:
                product = product*prod(nums[0:i])
            else:
                product = product*prod(nums[0:i])*prod(nums[i+1:])
            answer.append(product)
        return answer