class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left_1 = m - 1
        left_2 = n - 1
        while left_1 > -1 and left_2 > -1:
            if nums1[left_1] > nums2[left_2]:
                nums1[left_1 + left_2 + 1] = nums1[left_1]
                left_1 -= 1
            else:
                nums1[left_1 + left_2 + 1] = nums2[left_2]
                left_2 -= 1
        while left_1 > -1:
            nums1[left_1 + left_2 + 1] = nums1[left_1]
            left_1 -= 1
        while left_2 > -1:
            nums1[left_1 + left_2 + 1] = nums2[left_2]
            left_2 -= 1
        return nums1
