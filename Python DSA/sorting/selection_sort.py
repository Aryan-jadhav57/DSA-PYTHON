def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        # Swap
        nums[i], nums[min_index] = nums[min_index], nums[i]

# Example usage
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(arr)   # Output: [11, 12, 22, 25, 64]