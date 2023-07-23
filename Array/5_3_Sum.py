# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Notice that the order of the output and the order of the triplets does not matter.


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()

        # Seprating the numbers into three types: positive, negative and a zero counter
        n, p, z = [], [], 0
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z += 1
        
        # Removing duplicate numbers to check faster
        N, P = set(n), set(p)
        
        # If one zero is present we check the combination (-num, 0, num) and if we have more than 3 zeros than we add (0, 0, 0) one time
        if z:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))
            if z > 2:
                res.add((0, 0, 0))
        
        # For all the 2 number combination of negative numbers we check if -(sum of that combination) is present in the set of positive numbers
        for x, y in itertools.combinations(n, 2):
            target = -(x + y)
            if target in P:
                res.add(tuple(sorted([x, y, target])))
        
        # For all the 2 number combination of positive numbers we check if -(sum of that combination) is present in the set of negative numbers
        for x, y in itertools.combinations(p, 2):
            target = -(x + y)
            if target in N:
                res.add(tuple(sorted([x, y, target])))
        
        return res