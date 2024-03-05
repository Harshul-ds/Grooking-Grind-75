def find_sum_of_three(nums, target):
    nums.sort()  # Step 1: Sort the array

    for i in range(len(nums) - 2):  # Step 2: Iterate through the array
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values
            continue

        j, k = i + 1, len(nums) - 1  # Step 3: Initialize two pointers

        while j < k:  # Step 3: Continue until pointers meet
            current_sum = nums[i] + nums[j] + nums[k]

            if current_sum == target:  # Step 3: Check if the sum equals the target
                return True
            elif current_sum < target:  # Step 3: Increment `j` if sum is too small
                j += 1
            else:  # Step 3: Decrement `k` if sum is too large
                k -= 1

    return False 


