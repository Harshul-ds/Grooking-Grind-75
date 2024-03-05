def is_palindrome(s):
    left, right = 0, len(s) - 1  # Initialize two pointers
    while left < right:  # Continue until they meet in the middle
        if s[left] != s[right]:
            return False  # Characters at pointers don't match
        left, right = left + 1, right - 1  # Move pointers towards the center
    return True  # All characters matched, it's a palindrome
