import numpy as np

# Example coefficients of a quadratic polynomial: x^2 - 10x + 25
coefficients = [1, -10, 25]

# Evaluate the polynomial at the point (x-5)(x-5)
point = np.array([5])  # The point (x-5)(x-5) for x = 5
result = np.polyval(coefficients, point)

print(result)

