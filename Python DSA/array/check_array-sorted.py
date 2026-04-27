def check_array_sorted(nums):
    n = len(nums)
    for i in range(0, n-1):
        if nums[i]>nums[i+1]:
            return False
    return True
    
nums = [3,5,6,8,19,10]
print(check_array_sorted(nums)) 


# TC is O(n)
# SC is O(1) 
