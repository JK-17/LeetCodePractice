class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["+","-","*","/"]:
                second = stack.pop()
                first = stack.pop()
                num = getCal(first, second, i)
                stack.append(num)
            else:
                stack.append(int(i))

        return stack[0]

def getCal(first, second, operator):
    if operator == "+":
        return first + second
    elif operator == "-":
        return first - second
    elif operator == "*":
        return first * second
    elif operator == "/":
        return int(first / second)


