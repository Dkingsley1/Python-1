def is_palindrome(s):
    # Base cases
    if len(s) <= 1:
        return True

    # Compare first and last characters
    if s[0] != s[-1]:
        return False
    # Recursive call on the substring
    return is_palindrome (s[1:-1])
