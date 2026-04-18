#brute force type

def factors_number(n):            #This defines a function named factors_number that takes one parameter n
  num = n                         #Here you assign the value of n to a new variable num.
  result =[]                      #Creates an empty list called result.
  
  for i in range(1,num + 1):      #Starts a loop with i going from 1 up to num (inclusive).
    if num % i == 0:              #Checks if i divides num without leaving a remainder.
      result.append(i)            #If the condition is true, add i to the result list.
  return result                   #After the loop finishes, return the list of factors

print(factors_number(10))         #Calls the function with n = 10.



# efficient and best method

def factors_numbers(n):
  num = n 
  result = []
  for i in range ( 1 , num // 2 + 1):  #Starts a loop with i going from 1 up to num // 2 (inclusive).
    if num % i == 0:
      result.append(i)
  result.append(num)
  return result

print(factors_numbers(10))


#optimal solution

from math import sqrt                         #Imports the sqrt (square root) function from Python’s math module.

def factors_number(n):
    num = n
    result = []
    for i in range(1,int(sqrt(num))+1):       #Loops through numbers from 1 up to the integer value of the square root of num.
        if num % i == 0:
            result.append(i)
            if num // i != i:                 #Example: If i = 2 divides 36, then 36 // 2 = 18 is also a factor
                result.append(num // i)
    result.sort()                             #Sorts the list of factors in ascending order.
    return result
    
print(factors_number(36))