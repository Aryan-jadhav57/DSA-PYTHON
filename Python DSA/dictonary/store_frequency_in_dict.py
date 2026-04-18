#type 1 
def Frequency_map(n):
    nums = [5,6,7,7,8,5,6,3,2]
    Frequency_map = dict()                      #A new empty dictionary is created and stored in the variable Frequency_map
    for i in range(0,len(nums)):
        if nums[i] in Frequency_map:
            Frequency_map[nums[i]] += 1
        else:
            Frequency_map[nums[i]] = 1
    return Frequency_map    

print(Frequency_map(None))                #The function is called with None as the argument.


#type 2-----shorter

from collections import Counter           #This imports the Counter class from Python’s built-in collections module.

nums = [5, 6, 7, 7, 8, 5, 6, 3, 2]
freq_map = Counter(nums)                  #You pass the list nums into Counter.
print(freq_map)

# time complexity = O(n) 
# space complexity = O(n)