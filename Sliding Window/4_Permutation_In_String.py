''' Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2. '''

'''
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
'''

# class Solution(object):
#     def checkInclusion(self, s1, s2):
#         start, end = 0, len(s1)-1
#         count_s1 = collections.Counter(s1)
#         while end < len(s2):
#             if collections.Counter(s2[start: end+1]) == count_s1:
#                 return True
#             start += 1
#             end += 1
#         return False

class Solution:
    def checkInclusion(self, s1, s2):  
        if len(s2) < len(s1):
            return False

        s1_counter = {}
        s2_counter = {}
        for char in "abcdefghijklmnopqrstuvwxyz":
            s1_counter[char] = 0
            s2_counter[char] = 0
        for char in s1:
            s1_counter[char] = s1_counter.get(char, 0) + 1

        start = 0
        for end, char in enumerate(s2):
            s2_counter[char] = s2_counter.get(char, 0) + 1
            windowSize = end - start + 1

            if windowSize == len(s1):
                if s1_counter == s2_counter:
                    return True
                s2_counter[s2[start]] -= 1
                start += 1
        return False







                