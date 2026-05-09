def count_digits(n):  #Creates a function named count_digits that accepts one parameter n (the number to analyze).
  num = n             #Makes a copy of the input number. num works inside the function while n stays unchanged.
  count = 0           #Initializes counter to track total digits found.
  while num > 0 :     #Loops until no digits remain (when num becomes 0).
    count+=1          #Increments counter by 1 for each digit discovered.
    num = num // 10   #Removes rightmost digit using integer division:
  return count        #Returns final digit count after loop completes.

n = int(input("enter the digits : "))   #takes input
print(count_digits(n))                  #Calls function with user input and prints result.

#time compplexity of this code is TC => O(log10(n))
