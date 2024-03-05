def container_with_most_water(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        # Calculate the area between the two lines
        width = right - left
        min_height = min(height[left], height[right])
        current_area = width * min_height

        # Update max_area if the current area is larger
        max_area = max(max_area, current_area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

