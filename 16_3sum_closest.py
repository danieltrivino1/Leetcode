# 16. 3Sum Closest
# Solution (two pointers):
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = math.inf
        suma = 0
        nums.sort()
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                diff = abs(target - (nums[i] + nums[left] + nums[right]))
                if diff < min_diff:
                    min_diff = diff
                    suma = nums[i] + nums[left] + nums[right]
                if nums[i] + nums[left] + nums[right] > target:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < target:
                    left += 1
                else:
                    return target
        return suma
