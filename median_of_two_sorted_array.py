class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        merged_arr = sorted(nums1 + nums2)
        length = len(merged_arr)

        halfed = length // 2
        
        if (length % 2 == 0):

            result = float(merged_arr[halfed - 1] + merged_arr[halfed]) / 2

        else:

            result = float(merged_arr[halfed])
        
        return result
