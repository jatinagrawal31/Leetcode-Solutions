'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs) == 0):
            return ""
        prefix = strs[0]
        for i in strs:
            temp = i[0:min(len(i), len(prefix))]
            counter = 0
            for j in range(len(temp)):
                if(temp[j] != prefix[j]):
                    break
                counter += 1
            prefix = prefix[0:counter]
            
        return (prefix)
                
            
            
