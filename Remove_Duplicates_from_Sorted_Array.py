'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        l = 0
        r = 1
        while(r < len(nums)):
            while(r < len(nums) and nums[l] != nums[r]):
                l += 1
                r += 1
            
            while(r < len(nums) and nums[l] == nums[r]):
                r += 1
            if(r < len(nums)):
                l += 1
                nums[l] = nums[r]
            
        return l + 1
            