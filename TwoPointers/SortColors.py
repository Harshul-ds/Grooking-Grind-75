def sort_colors(nums):
    low, i, high = 0, 0, len(nums) - 1

    while i <= high:
        if nums[i] == 0:
            nums[i], nums[low] = nums[low], nums[i]
            i += 1
            low += 1
        elif nums[i] == 2:
            nums[i], nums[high] = nums[high], nums[i]
            high -= 1
        else:  # nums[i] == 1
            i += 1

    return nums

