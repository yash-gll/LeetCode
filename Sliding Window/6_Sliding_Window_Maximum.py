""" You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window. """

"""
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        output = []
        maxQueue = collections.deque()
        left, right = 0, 0

        while right < len(nums):
            while maxQueue and nums[right] > maxQueue[-1]:
                maxQueue.pop()
            maxQueue.append(nums[right])

            # If Window is less than K move right
            if (right-left+1 < k):
                right += 1
            else:
                output.append(maxQueue[0])
                if nums[left] == maxQueue[0]:
                    maxQueue.popleft()
                left += 1
                right += 1

        return output