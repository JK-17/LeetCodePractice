class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        # find the backward, monotonic decrease stack
        for i in range(n - 1, -1, -1):

            # clear the stack until stack has the higher value
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            # stack not empty, update res
            if stack:
                res[i] = stack[-1] - i
            
            # append index in stack
            stack.append(i)

        return res
