# 1004. Max Consecutive Ones III
# Solution (sliding window):
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        curr = 0
        ans = 0
        for right in range(len(nums)):
            curr += (1 - nums[right])
            while curr > k:
                curr -= (1 - nums[left])
                left += 1
            ans = max(ans, right - left + 1)
        return ans
            
