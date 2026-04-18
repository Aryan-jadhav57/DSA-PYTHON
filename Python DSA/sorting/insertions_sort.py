def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    print(nums)   # <-- add this
    
insertion_sort([5, 3, 4, 1])
# Output: [1, 3, 4, 5]