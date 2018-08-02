'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if(i == '(' or i == '{' or i == '['):
                stack.append(i);
            else:
                if(len(stack) == 0):
                    return False
                temp = stack.pop()
                if(i == ')' and temp == '(' or
                   i == '}' and temp == '{' or
                   i == ']' and temp == '['): 
                    continue
                else:
                    return False
        if(len(stack) > 0):
            return False
        return True