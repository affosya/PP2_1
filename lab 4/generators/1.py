def generate_squares(N):
    for i in range(N+1):
        yield i * i

N = 5
squares = generate_squares(N)
for square in squares:
    print(square)
