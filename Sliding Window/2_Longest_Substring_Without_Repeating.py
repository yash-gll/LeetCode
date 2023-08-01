''' Given a string s, find the length of the longest substring without repeating characters. '''
'''
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

#METHOD - 1: USING A SET OR A LIST TO MAINTAIN VISITED
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        window = []
        start = 0
        end = 0
        ans = 0
        while end < len(s):
            if s[end] in window:
                ans = max(ans, len(window))
                while s[end] in window:
                    window.pop(0)
            window.append(s[end])
            end += 1
        ans = max(ans, len(window))
        return ans
    
#METHOD - 2: USING A DICTINARY TO MAINTAIN INDEXES OF VISITED
class Solution(object):
    def lengthOfLongestSubstring(self, s):
            used = {}
            max_length = start = 0
            for i, c in enumerate(s):
                if c in used and start <= used[c]:
                    start = used[c] + 1
                else:
                    max_length = max(max_length, i - start + 1)
                used[c] = i
            return max_length