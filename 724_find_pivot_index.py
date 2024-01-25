class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left = [0]
        for i in range(len(nums)-1):
            sum_left.append(sum_left[i] + nums[i])
        
        left = 0
        right = len(nums) - 1
        while left < right:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            left += 1
            right -= 1

        sum_right = [0]
        for i in range(len(nums)-1):
            sum_right.append(sum_right[i] + nums[i])
  
        left = 0
        right = len(sum_right) - 1
        while left < right:
            temp = sum_right[right]
            sum_right[right] = sum_right[left]
            sum_right[left] = temp
            left += 1
            right -= 1

        for i in range(len(nums)):
            if sum_left[i] - sum_right[i] == 0:
                return i
        
        return -1
