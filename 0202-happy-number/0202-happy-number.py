class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        while True:
            if count > 500:
                return False
            if n == 1:
                return True
            else:
                temp = 0
                for i in str(n):
                    temp += int(i)**2
                n = temp
                count += 1
        