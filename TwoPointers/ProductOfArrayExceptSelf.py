def product_except_self(arr):
    n = len(arr)
    
    # Initialize the left, right, and result arrays
    left = [1] * n
    right = [1] * n
    res = [1] * n

    # Fill in the left array
    for i in range(1, n):
        left[i] = arr[i - 1] * left[i - 1]

    # Fill in the right array
    for i in range(n - 2, -1, -1):
        right[i] = arr[i + 1] * right[i + 1]

    # Calculate the result array
    for i in range(n):
        res[i] = left[i] * right[i]

    return res

