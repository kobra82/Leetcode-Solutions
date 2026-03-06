# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

# Example 1:

# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
# Example 2:

# Input: arr = [1,1]
# Output: 1
 

# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 105

class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        limit = round(len(arr)/4)
        output = 0
        integer = 1
        if len(arr) == 1:
            return arr[0]
        else:
            for i in range(len(arr)-1):
                if (arr[i]==arr[i+1]):
                    integer+=1
                    if (integer >= limit):
                        output = arr[i]
                else:
                    if (integer >= limit):
                        output = arr[i]
                    integer = 1
        return output