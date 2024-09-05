def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example: Factorial of 5
result = factorial_recursive(5)
print("Factorial (Recursive):", result)



def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example: Factorial of 5
result = factorial_iterative(5)
print("Factorial (Iterative):", result)
