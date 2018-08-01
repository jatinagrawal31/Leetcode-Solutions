'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''

class Solution(object):
    def checkPallindrome(self, s, i, j):
        length = 0
        while(True):
            if(i < 0 or j >= len(s) or s[i] != s[j]):
                return length
            if(s[i] == s[j]):
                length += 2
            i-= 1
            j += 1
                
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        center = 0
        maxCenter = 0
        maxLength = 0
        while center < len(s):
            lengthCenter1 = 1 + self.checkPallindrome(s, center - 1, center + 1)
            lengthCenter2 = self.checkPallindrome(s, center , center + 1)
            
            if(lengthCenter1 > lengthCenter2 and lengthCenter1 > maxLength):
                maxCenter = center
                maxLength = lengthCenter1
                
            if(lengthCenter2 > lengthCenter1 and lengthCenter2 > maxLength):
                maxCenter = center
                maxLength = lengthCenter2
            center += 1
        

        if(maxLength%2 == 0):
            return s[maxCenter - int(maxLength-1)/2 : maxCenter + int(maxLength/2)+1]
        return s[maxCenter - int(maxLength/2) : maxCenter + int(maxLength/2)+1]
