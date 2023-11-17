# This is y     
def your_function(x):
    return x**2 - 2

# This is dy/dx
def your_derivative(x):
    return 2*x

def nm(initial_guess): #newton's method
    x = initial_guess   
    y = your_function(x)
    for iterator in range(20):
        f_x = your_function(x)
        f_prime_x = your_derivative(x)

        if abs(f_x) < 1e-6:
            return x  # Convergence reached

        x = x - f_x / f_prime_x

    return None  # If max_iterations reached without convergence

print(nm(2))

# Example usage:
# initial_guess = 1
# tolerance = 1e-6
# max_iterations = 100

# result = newton_method(initial_guess))

# if result is not None:
#     print(f"Newton's method converged to: {result}")
# else:
#     print("Newton's method did not converge within the specified iterations.")

