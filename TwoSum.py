'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #brute force, check index 0 , compare every other index to find target
        #look at index value, search if the additive is present in the list
        #time complexity n^2 using nested for loop
        
        
        for i in range(len(nums)):
            needtarget = target - nums[i]
            for j in range(len(nums)):
                if needtarget == nums[j] and i != j: #duplicate check
                    return i, j
