class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # transform list to set
        numSet = set(nums)
        # longest consequence
        res = 0
        # loop nums
        for i in numSet:
            # is this number can be the start of sequence
            if (i-1) not in numSet:
                # search length of consequence
                length = 1
                while (i + length) in numSet:
                    length += 1
                # compare with any length was biggest previously
                res = max(length, res)

        return res
            
        