def largestRectangleArea(heights):
    stack = []  # Initialize an empty stack
    max_area = 0  # Max area starts at 0
    
    for i, h in enumerate(heights + [0]):  # Add a zero height bar at the end to ensure all bars are popped
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]  # Height of the rectangle
            width = i if not stack else i - stack[-1] - 1  # Width of the rectangle
            max_area = max(max_area, height * width)  # Update max_area if necessary
        stack.append(i)
    
    return max_area

