''' You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations. '''

'''
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
'''

class Solution(object):
    def characterReplacement(self, s, k):
        charDict = {}
        start = 0
        end = 0
        maxCount = 0
        curr = 0
        ans = 0
        for end in range(len(s)):
            charDict[s[end]] = charDict.get(s[end], 0) + 1
            maxCount = max(maxCount, charDict[s[end]])
            if curr - maxCount < k:
                ans = max(ans, end-start+1)
                curr += 1
                end += 1
            else:
                charDict[s[start]] -= 1
                start += 1
        return ans