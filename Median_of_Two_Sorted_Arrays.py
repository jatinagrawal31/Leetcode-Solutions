'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1Median = num1[int(len(nums1)/2)]
        nums2Median = num2[int(len(nums2)/2)]

        if(nums2Median == nums1Median):
        	return nums1Median
       	elif(len(nums1) == 1):
       		return nums1[0]
       	elif(len(nums2) == 1):
       		return nums2[0]
        elif(nums1Median > nums2Median):
        	findMedianSortedArrays(nums1[:int(len(nums1)/2)], nums2Median[int(len(nums2)/2):])
        else:
        	findMedianSortedArrays(nums1[int(len(nums1)/2):], nums2Median[:int(len(nums2)/2)])
