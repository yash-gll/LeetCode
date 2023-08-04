""" Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type. """

"""
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""

class Solution(object):
    def isValid(self, s):
        stack = []
        isValid = True
        for b in s:
            if b == "(" or b == "{" or b =="[":
                stack.append(b)
            else:
                if not stack:
                    isValid = False
                elif b == ")" and stack[-1] == "(":
                    stack.pop()
                elif b == "}" and stack[-1] == "{":
                    stack.pop()
                elif b == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    isValid = False
        if isValid and stack:
            isValid = False

        return isValid