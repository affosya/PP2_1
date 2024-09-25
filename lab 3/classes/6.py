def is_prime(n):
    if n <= 1:
        return False  # Numbers <= 1 are not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # If divisible by any number, it's not prime
    return True  # It's prime

# List of numbers
numbers = [1, 2, 3, 4, 5, 16, 17, 18, 19]
# Filter prime numbers using a simple loop
prime_numbers = [num for num in numbers if is_prime(num)]

print("Prime numbers:", prime_numbers)  # Output the list of prime numbers
