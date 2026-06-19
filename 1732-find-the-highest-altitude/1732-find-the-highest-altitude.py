class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        calculate_li = [0]

        for i in gain:
            calculate_li.append(calculate_li[-1] + i)

        return max(calculate_li)