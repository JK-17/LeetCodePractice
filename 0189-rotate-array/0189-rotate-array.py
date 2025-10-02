class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for _ in range(k):
            if nums[0] >= 0:
                nums.insert(0, nums[-1])
                nums.pop()
            else:
                nums.append(nums[0])
                nums.pop(0)

        