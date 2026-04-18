def check_palindrome(n):
    original_n = n      # Save original number
    num = n             # Working copy  
    result = 0          # Reversed number
    while num > 0:
        Ld = num % 10   # Last digit (4, 3, 2, 1)
        result = (result * 10) + Ld  # Build reverse: 0→4→43→432→4321
        num = num // 10  # Remove last digit
    return original_n == result

n = int(input("enter the number ; "))
print(check_palindrome(n))  # Output: False


#type 2
class Solution:
    def isPalindrome(self, x: int):
        if x < 0:
            return False
        
        original = x
        reversed_num = 0
        
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        return original == reversed_num