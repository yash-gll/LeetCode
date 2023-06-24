# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. 

# My Solution - O(n) | Runtime: 87.75% | Memory: 5.39%
class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
    

# Best Solution - O(n) | Runtime: 95.75% | Memory: 82.39%
class Solution(object):
    def containsDuplicate(self, nums):
        dict = {}
        for n in nums:
            if n in dict:
                return True
            else:
                dict[n] = 1