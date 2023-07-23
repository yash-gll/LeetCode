'''Approach-1: Using Two Pointers'''

class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if curr < 0:
                    left += 1
                elif curr > 0:
                    right -= 1
                else:
                    if [nums[i], nums[left], nums[right]] not in res:
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1
                right -= 1
        return res
    
'''Approach-2: Using sets'''
class Solution(object):
    def threeSum(self, nums):
        res = set()
        n, p, z = [], [], 0
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z += 1
        
        N, P = set(n), set(p)
        
        if z:
            if z > 2:
                res.add((0, 0, 0))
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))
              
        for x, y in itertools.combinations(n, 2):
            target = -(x + y)
            if target in P:
                res.add(tuple(sorted([x, y, target])))
        
        for x, y in itertools.combinations(p, 2):
            target = -(x + y)
            if target in N:
                res.add(tuple(sorted([x, y, target])))
    
        return res