class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # scan O(n)
        for num in numbers:
            # find differnce in numbers[int]
            diff = target - num
            index1 = numbers.index(num) + 1

            if diff in numbers:
                return [index1, numbers.index(diff, index1, len(numbers)) + 1]
        return []