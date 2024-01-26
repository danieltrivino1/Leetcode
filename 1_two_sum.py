class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {nums[0]: 0}
        for i in range(1, len(nums)):
            if target - nums[i] in dictionary:
                return [dictionary[target - nums[i]], i]
            else:
                dictionary[nums[i]] = i
