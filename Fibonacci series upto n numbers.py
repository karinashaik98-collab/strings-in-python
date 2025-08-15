def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
num_terms = 10
print(f"Fibonacci series up to {num_terms} terms:")
fibonacci(num_terms)
