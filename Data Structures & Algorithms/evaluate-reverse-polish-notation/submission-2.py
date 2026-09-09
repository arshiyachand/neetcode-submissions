class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "-":
                second, first = stack.pop(),stack.pop()
                stack.append(first-second)
            elif i == "/":
                second, first = stack.pop(),stack.pop()
                stack.append(int(first/second))
            else:
                stack.append(int(i))

        print(stack)

        return stack[0]


        