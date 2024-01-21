# 209. Minimum Size Subarray Sum
# Solution (slidding window):
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        window_sum = 0
        result = 0
        while (window_sum < target) and (right < len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                if result == 0:
                    result = right - left + 1
                else:
                    result = min(result, right - left + 1)
                window_sum -= nums[left]
                left += 1
            right += 1
        return result             
