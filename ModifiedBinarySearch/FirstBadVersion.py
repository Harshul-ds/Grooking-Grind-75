def isBadVersion(version):
    # This is a placeholder for the actual API call.
    # Returns True if the version is bad, False otherwise.
    pass

def findFirstBadVersion(n):
    start, end = 1, n
    api_calls = 0  # To track the number of API calls

    while start < end:
        mid = (start + end) // 2
        api_calls += 1  # Increment API call count

        if isBadVersion(mid):
            end = mid  # The first bad version is at `mid` or before it.
        else:
            start = mid + 1  # The first bad version is after `mid`.

    # `start` is now pointing to the first bad version.
    return start, api_calls  # Return the first bad version and the number of API calls.
