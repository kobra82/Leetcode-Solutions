# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                if i == 0:
                    nums = nums[i+1:]
                    nums.append(0)
                elif i == len(nums)-1:
                    pass
                else:
                    nums = nums[0:i] + nums[i+1:]
                    nums.append(0)
        print(nums)

solution = Solution()
print(solution.moveZeroes([0]))
print(solution.moveZeroes([0,1,0,3,12]))