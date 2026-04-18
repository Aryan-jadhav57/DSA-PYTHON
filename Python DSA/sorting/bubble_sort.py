def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):  # outer loop
        is_swap = False
        for j in range(0, n-i-1):  # inner loop
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swap = True
        if not is_swap:  # optimization: stop if already sorted
            break

# Example usage
arr = [64, 25, 12, 22, 11]
bubble_sort(arr)
print(arr)   # Output: [11, 12, 22, 25, 64]