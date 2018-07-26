'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        start = 0
        longest = 0
        for i, j in enumerate(s):
            if j in hashmap:
                if hashmap[j] >= start:
                    longest = max(longest, i - start)
                    start = hashmap[j] + 1
            hashmap[j] = i
        longest = max(longest, len(s) - start )
        return longest