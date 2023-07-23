"O(n) memory solution"
class Solution(object):
    def trap(self, height):
        maxLeft, maxRight = [0]*len(height), [0]*len(height)
        currMaxLeft, currMaxRight, i, j = 0, 0, 0, len(height)-1
        while i < len(height):
                maxLeft[i] = currMaxLeft
                currMaxLeft = max(currMaxLeft, height[i])
                i += 1
                
        while j >= 0:
            maxRight[j] = currMaxRight
            currMaxRight = max(currMaxRight, height[j])
            j -= 1

        ans = 0
        for i in range(len(height)):
            curr = min(maxLeft[i], maxRight[i]) - height[i]
            if curr > 0:
                ans += curr
        return ans
    
"O(1) memory solution"
class Solution(object):
    def trap(self, height):
        left, right = 0, len(height)-1
        water = 0
        lmax, rmax = 0, 0
        while left < right:
            lh = height[left]
            rh = height[right]
            if lh < rh:
                if lh > lmax:
                    lmax = lh
                else:
                    water += lmax - lh
                left += 1
            else:
                if rh > rmax:
                    rmax = rh
                else:
                    water += rmax - rh
                right -= 1
        return water