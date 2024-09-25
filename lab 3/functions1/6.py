def has_33(nums):
    # Loop through the list, checking for consecutive 3s
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Example usage:
print(has_33([1, 3, 3]))       # → True
print(has_33([1, 3, 1, 3]))    # → False
print(has_33([3, 1, 3]))       # → False
