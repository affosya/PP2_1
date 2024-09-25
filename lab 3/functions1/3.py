def solve(numheads, numlegs):
    # Equation 1: c + r = numheads
    # Equation 2: 2c + 4r = numlegs
    
    for r in range(numheads + 1):  # Iterate over possible number of rabbits
        c = numheads - r           # Calculate the number of chickens
        if 2 * c + 4 * r == numlegs:  # Check if the solution satisfies the leg equation
            return c, r
    
    return None  # If no solution is found

# Example usage:
numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)

if chickens is not None:
    print(f"Number of chickens: {chickens}, Number of rabbits: {rabbits}")
else:
    print("No solution found")
