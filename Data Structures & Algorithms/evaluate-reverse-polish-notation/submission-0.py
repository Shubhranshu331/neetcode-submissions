class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        operators= {'+','-','*','/'}
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                right=stack.pop()
                left=stack.pop()

                if i == '+':
                    stack.append(left+right)
                elif i == '-':
                    stack.append(left-right)
                elif i == '/':
                    stack.append(int(left/right))
                else:
                    stack.append(left*right)
        return stack.pop()