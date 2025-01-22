import numpy as np
from scipy.stats import norm

# Inputs
mean = 0
std = 1

# Generate x values
x = np.linspace(mean - 4 * std, mean + 4 * std, 100)

# Calculate PDF
y = norm.pdf(x, mean, std)

# Print results
for i in range(len(x)):
    print(f"x: {x[i]:.2f}, f(x): {y[i]:.5f}")
