# 26. Remove Duplicates from Sorted Array
# Solution 1 (three pointers):
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        k = 1
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1
                k += 1
        return k
# Solution 2 (two pointer):
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        k = 1
        while left < len(nums):
            if nums[left] == nums[left - 1]:
                left += 1
            else:
                nums[k] = nums[left]
                left += 1
                k += 1
        return k
