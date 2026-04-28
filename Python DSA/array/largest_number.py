def largest_number(nums):
    largest = float("-inf")
    n = len(nums)
    for i in range(0, n):
        largest = max(largest, nums[i])
    return largest

nums = [12, 3, 55, 99, -87]
print(largest_number(nums)) 
