# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# My Solution - O(nlogn) | Runtime: 47.17% | Memory: 45.39%
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

# Better Solution - O(n) | Runtime: 78.75% | Memory: 7.39%
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        dictS, dictT = {}, {}
        for i in range(len(s)):
            dictS[s[i]] = dictS.get(s[i], 0) + 1
            dictT[t[i]] = dictT.get(t[i], 0) + 1
            
        for letter in dictS:
            if dictS[letter] != dictT.get(letter, 0):
                return False
        return True
    
# Best Solution - O(n) | Runtime: 99.42% | Memory: 82.61%
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): 
            return False
        else:
            letters = "abcdefghijklmnopqrstuvwxyz"
            for letter in letters:
                if s.count(letter) != t.count(letter):
                    return False
        return True