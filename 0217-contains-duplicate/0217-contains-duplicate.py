class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums):
            preNum = nums[0]
            del nums[0]
        for i in nums:
            if preNum == i:
                return True
            else:
                preNum = i
        return False