class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key= lambda x:len(x))
        first_str = strs[0]
        res = ""

        for index, value in enumerate(first_str):
            check = True
            for data in strs:
                if data[index] != value:
                    check = False
            
            if check:
                res += value
            else:
                break
                
        return res
        
