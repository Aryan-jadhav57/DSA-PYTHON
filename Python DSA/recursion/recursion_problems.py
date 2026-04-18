# print aryan 4 times usuing recursion   ------- head recursion ------- first job is eexceutated and thn function is called 

def countt_no(count = 0):
  if count == 4:
    return
  print("aryan")
  countt_no(count + 1)

countt_no()



# tail recursion 
def countt_no(count = 0):
  if count == 4:
    return
  countt_no(count + 1)
  print("aryan")
  

countt_no()




#using parameters
def func(x,N):
    if N == 0:
        return
    print(x)
    func(x,N-1)
func(15,4)


# print 1 to N using recursion
def func(i,N):
    if i > N:
        return
    print(i)
    func(i+1,N)
    
func(1,4)


#usuing backtracking
def func(i,N):
    if i > N:
        return
    func(i+1,N)
    print(i)
    
    
func(1,4)


# N to 1
def func(N):
    if N == 0:
        return
    print(N)
    func(N-1)
    
func(4)


#sum of 1 to N 
def func(sum,i,N):
    if i > N:
        print(sum)
        return
    func(sum+i,i+1,N)
    
func(0,1,4)



#functional recursion
def func(N):
    if N == 1:
        return 1
    return N + func(N-1)
    

print(func(10))


# factorial of number usuing recursion
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num*(factorial(num-1))
    
print(factorial(5))


#reverse a string usuing recursion

def reverseArray(nums, left, right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    reverseArray(nums, left + 1, right - 1)

nums = [2, 5, 7, 4, 9, 3, 5, 3, 7, 4]
reverseArray(nums, 2, 8)
print(nums)



#Check if a String is Palindrome or No
def isPalindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return isPalindrome(s, left + 1, right - 1)

s = "NITIN"
result = isPalindrome(s, 0, len(s) - 1)
print("NITIN is a" ,result)



#fibonacci series using recursion
class Solution:
    def func(self, num):
        if num == 0 or num == 1:
            return num
        return self.func(num-1) + self.func(num-2)
    
    def fib(self, n: int):
        answer = self.func(n)
        return answer

# Create an object of the class
s = Solution()

# Call the method and print the result
print(s.fib(5))   # Output: 5
print(s.fib(10))  # Output: 55 answer


