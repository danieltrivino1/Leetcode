# 283. Move Zeroes
# Solution (two pointers | inefficient):
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            right = i
            while (nums[right] == 0) and (right < len(nums) - 1):
                right += 1
            temp = nums[i]
            nums[i] = nums[right]
            nums[right] = temp
        return nums
# Solution (two pointers | efficient):
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0 and nums[left] == 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
            if nums[left] != 0:
                left += 1
