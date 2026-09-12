"""
LeetCode Problem 9: Palindrome Number
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.

Time Complexity: O(log(x)) - Number of digits in x
Space Complexity: O(1) - Constant extra space
"""

def is_palindrome(x: int) -> bool:
    """
    Check if an integer is a palindrome.
    
    Args:
        x: Integer to check
        
    Returns:
        True if x is palindrome, False otherwise
    """
    # Negative numbers are not palindromes
    # Numbers ending with 0 (except 0 itself) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    # When the length is an odd number, we can get rid of the middle digit by reversed_half // 10
    return x == reversed_half or x == reversed_half // 10

# Alternative string-based solution
def is_palindrome_string(x: int) -> bool:
    """
    String-based approach to check palindrome.
    
    Time Complexity: O(log(x))
    Space Complexity: O(log(x)) - for string conversion
    """
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

# Test cases
if __name__ == "__main__":
    # Test case 1
    x1 = 121
    print(f"Input: x = {x1}")
    print(f"Output: {is_palindrome(x1)}")  # Expected: True
    print()
    
    # Test case 2
    x2 = -121
    print(f"Input: x = {x2}")
    print(f"Output: {is_palindrome(x2)}")  # Expected: False
    print()
    
    # Test case 3
    x3 = 10
    print(f"Input: x = {x3}")
    print(f"Output: {is_palindrome(x3)}")  # Expected: False
    print()
    
    # Test case 4
    x4 = -101
    print(f"Input: x = {x4}")
    print(f"Output: {is_palindrome(x4)}")  # Expected: False
    print()
    
    # Test case 5
    x5 = 0
    print(f"Input: x = {x5}")
    print(f"Output: {is_palindrome(x5)}")  # Expected: True