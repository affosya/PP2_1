def spy_game(nums):
    # Initialize a variable to track the sequence of 0s and 7
    sequence = []
    
    for num in nums:
        if num == 0:
            sequence.append(0)
        elif num == 7:
            sequence.append(7)
        
        # If we have two 0s followed by a 7, return True
        if sequence == [0, 0, 7]:
            return True
    
    return False

# Example usage:
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # --> True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # --> True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # --> False
