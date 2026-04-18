# brute force method

def Remove_duplicate(nums):
    n = len(nums)
    freq_map = {}
    for i in range(0,n):
        freq_map[nums[i]] = 0
    j = 0
    
    for k in freq_map:
        nums[j] = k
        j+=1
        
    return j
    
n = [1,1,1,2,3,4,4,7,9,9,9,10]
print(Remove_duplicate(n))

# TC = 0(2N) = 0(N)
# sC = 0(2N) = 0(N)



# usuing points and swapping
def Remove_duplicate(nums):
    n = len(nums)
    if n == 1:
        return 1
    i = 0
    j = i+1
    
    while j < n:
        if nums[j]!= nums[i]:
            i +=1
            nums[i],nums[j] = nums[j],nums[i]
        j +=1
    return i+1
    
n = [1,1,1,2,3,4,4,7,9,9,9,10]
print(Remove_duplicate(n))

# TC = 0(2N) = 0(N)
# sC = 0(2N) = 0(1)