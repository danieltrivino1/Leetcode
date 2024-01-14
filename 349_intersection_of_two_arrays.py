# 349. Intersection of Two Arrays
# Solution (two pointers):
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        left_1 = 0
        left_2 = 0
        while left_1 < len(nums1) and left_2 < len(nums2):
            if nums1[left_1] in nums2:
                result.add(nums1[left_1]) 
            left_1 += 1
            left_2 += 1
        while left_1 < len(nums1):
            if nums1[left_1] in nums2:
                result.add(nums1[left_1]) 
            left_1 += 1
        while left_2 < len(nums2):
            if nums2[left_2] in nums1:
                result.add(nums2[left_2]) 
            left_2 += 1
        result = list(result)
        return result
      
