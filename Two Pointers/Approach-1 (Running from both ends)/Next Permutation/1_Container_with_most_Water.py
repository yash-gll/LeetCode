class Solution(object):
    def maxArea(self, height):
        start, end, res = 0, len(height)-1, 0
        while start < end:
            area = (end - start) * min(height[start], height[end])
            res = max(res, area)
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return res

            