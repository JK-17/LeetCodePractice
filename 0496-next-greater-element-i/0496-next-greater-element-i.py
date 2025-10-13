class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            find_index = nums2.index(i)
            answer = -1
            for j in range(find_index, len(nums2)):
                if nums2[j] > i:
                    answer = nums2[j]
                    break
            res.append(answer)

        return res

