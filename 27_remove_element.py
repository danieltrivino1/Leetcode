# 27. Remove Element
# Solution (two pointers):
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = 0
        k = 0
        while right < len(nums):
            if nums[right] != val:
                nums[k] = nums[right]
                right += 1
                k += 1
            else:
                right += 1
        return k
