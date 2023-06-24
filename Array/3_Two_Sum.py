# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# My Solution - O(n^2) | Runtime: 47.17% | Memory: 45.39%
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in nums and nums.index(rem) != i:
                return [i, nums.index(rem)]
            
# Best Solution - O(n) | Runtime: 99.42% | Memory: 82.61%
class Solution(object):
    def twoSum(self, nums, target):
        t = {}
        for i in range(len(nums)):
            if nums[i] not in t:
                t[target-nums[i]] = i
            else:
                return [i, t[nums[i]]]