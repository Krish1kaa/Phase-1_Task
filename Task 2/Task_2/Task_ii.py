import matplotlib.pyplot as plt
import numpy as np

# Sample data
np.random.seed(0)  # For reproducibility
x = np.random.rand(100)  # 100 random values for x
y = 2 * x + np.random.normal(0, 0.1, 100)  # y is a function of x with some noise

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, c='blue', edgecolor='k', alpha=0.7)
plt.title('Scatter Plot of x vs y')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)  # Adds a grid for better readability
plt.show()
