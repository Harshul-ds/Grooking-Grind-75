def calculate(s):
    stack = []
    operand = 0
    result = 0  # For the on-going result
    sign = 1  # 1 means positive, -1 means negative  
    
    for ch in s:
        if ch.isdigit():
            operand = (operand * 10) + int(ch)
        elif ch == '+':
            result += sign * operand
            sign = 1
            operand = 0
        elif ch == '-':
            result += sign * operand
            sign = -1
            operand = 0
        elif ch == '(':
            # Push the result and sign onto the stack, for later
            stack.append(result)
            stack.append(sign)
            # Reset the sign and result for the new sub-expression
            sign = 1
            result = 0
        elif ch == ')':
            # Finish the sub-expression and get the result
            result += sign * operand
            result *= stack.pop()  # stack.pop() is the sign before the parenthesis
            result += stack.pop()  # stack.pop() now is the result calculated before the parenthesis
            operand = 0

    return result + sign * operand  # There may be a number in the end

