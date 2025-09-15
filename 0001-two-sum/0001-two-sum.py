class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Goal => timecomplexity O(n)
        # use dictionary
        hashMap = {}
        # use enumerate to find index(i), and value (num) in array (nums)
        for i, num in enumerate(nums):
            # subtract to find correspoding value
            diff = target - num
            # if there is in the dictionary (means you know where(index) and what(value))
            if diff in hashMap:
                # return it with the value
                return [hashMap[diff], i]
            # else (there is no corresponding value in dictionary)
            # append them in dictionary (for next compare or to find the answer)
            hashMap[num] = i