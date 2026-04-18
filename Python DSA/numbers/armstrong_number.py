def arm_strong(n):     #defines the function
  num = n               #Creates a copy of n called num.
  total = 0             #Initializes a variable total to store the sum of digits raised to a certain power.
  nod = len(str(n))     #Converts n to a string, finds its length, and stores it in nod
  while num > 0 :       #Runs a loop until num becomes 0.
    Last_digit = num % 10   # % 10 gives the last digit of num.
    total = total + (Last_digit**nod)       #Raises the digit Ld to the power of nod and adds it to total.
    num = num // 10       #Integer division by 10 removes the last digit.        
  return total == n       #After the loop, checks if the sum of powered digits (total) equals the original number n.

n =  int(input("enter the number to check :"))
print(arm_strong(n))
