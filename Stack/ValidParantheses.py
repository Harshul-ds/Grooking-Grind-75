def isValid(s):
    stack = []
    # Mapping of closing to opening parentheses
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in mapping:  # If it's a closing parenthesis
            # Pop the top of the stack if it's not empty, otherwise use a dummy value
            top_element = stack.pop() if stack else '#'
            
            # If the popped element is not the corresponding opening parenthesis, return False
            if mapping[char] != top_element:
                return False
        else:
            # If it's an opening parenthesis, push onto the stack
            stack.append(char)
    
    # If the stack is empty, all parentheses were closed properly
    return not stack

