class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            
            if (token.startswith('-') and (token[1:].isnumeric())) or (token.isnumeric()):
                stack.append(int(token))
            else:
                if token=='+':
                    res = stack[-2]+stack[-1]
                elif token=='-':
                    res = stack[-2]-stack[-1]
                elif token=='*':
                    res = stack[-2]*stack[-1]
                elif token=='/':
                    res = stack[-2]/stack[-1]
                
                    
                stack.pop()
                stack.pop()
                stack.append(int(res))

        return stack[0]
