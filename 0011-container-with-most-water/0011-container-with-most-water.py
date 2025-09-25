class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers
        left, right = 0, len(height) -1

        # first area
        res = min(height[left], height[right]) * (right - left)
        # O(n) => scan
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            area = min(height[left], height[right]) * (right - left)
            res = max(res, area)

        return res