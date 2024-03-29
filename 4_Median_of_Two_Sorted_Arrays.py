# Accepted 82ms, 17.59MB
'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the 
median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = (nums1 + nums2)
        nums.sort()
        m = len(nums)//2
        if(len(nums) % 2 == 0):
            return(nums[m] + nums[m-1])/2
        else:
            return nums[m]