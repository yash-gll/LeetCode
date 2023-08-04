''' Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique. '''

'''
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
'''

class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""
        t_counter, s_counter = {}, {}
        for c in t:
            t_counter[c] = t_counter.get(c, 0) + 1
        
        left = 0
        have, need = 0, len(t_counter)
        result, result_length = [-1, -1], float('inf')
        for right in range(len(s)):
            c = s[right]
            s_counter[c] = s_counter.get(c, 0) + 1
            if c in t_counter and s_counter[c] == t_counter[c]:
                have += 1
            
            while have == need:
                if (right-left+1) < result_length:
                    result_length = right-left+1
                    result = [left, right]
                s_counter[s[left]] -= 1
                if s[left] in t_counter and s_counter[s[left]] < t_counter[s[left]]:
                    have -= 1
                left += 1
        return s[result[0]: result[1]+1]