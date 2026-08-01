class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
             num2 = {}
             for i in range(len(nums)):
                difference = target - nums[i]
                if difference in num2:
                    return [num2[difference], i]
                num2[nums[i]] = i

