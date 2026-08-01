class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num2 = set()
        for x in nums:
            num2.add(x)

        if len(num2) < len(nums):
            return True

        return False
