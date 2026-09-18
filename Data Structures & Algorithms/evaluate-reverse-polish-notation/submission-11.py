class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        stack = []
        for token in tokens:
            match token:
                case '+':
                    var1 = stack.pop()
                    var2 = stack.pop()
                    result = var1 + var2
                    stack.append(result)
                case '-':
                    var1 = stack.pop()
                    var2 = stack.pop()
                    result = var2 - var1
                    stack.append(result)
                case '*':
                    var1 = stack.pop()
                    var2 = stack.pop()
                    result = var1 * var2
                    stack.append(result)
                case '/':
                    var1 = stack.pop()
                    var2 = stack.pop()
                    result = int(float(var2) / var1)
                    stack.append(result)
                case _:
                    stack.append(int(token))
        return stack.pop()