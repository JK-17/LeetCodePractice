class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ''
        for digit in digits:
            temp += str(digit)

        temp = str(int(temp) + 1)
        res = []
        for s in temp:
            res.append(int(s))
        
        return res
