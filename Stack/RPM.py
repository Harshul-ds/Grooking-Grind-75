def evalRPN(tokens):
    stack = []
    
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            # Pop the last two operands from the stack
            b, a = stack.pop(), stack.pop()
            
            # Apply the operator
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                # Note: int division in Python truncates towards less, so we add this to mimic "towards zero" behavior.
                result = int(float(a) / b)
            
            # Push the result back onto the stack
            stack.append(result)
        else:
            # Token is an operand, push onto the stack
            stack.append(int(token))
    
    # The final result is the only element left in the stack
    return stack.pop()

