class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(' ')
        print(arr)

        i = len(arr) - 1

        while i >= 0:
            if arr[i] != '':
                return len(arr[i])
            
            i -= 1
        
        return 0