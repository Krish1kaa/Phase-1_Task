import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# Sample data
data = np.random.randn(1000)  # Generating 1000 random data points

# Creating a figure with two subplots
fig, ax = plt.subplots(1, 2, figsize=(15, 6))

# Histogram
ax[0].hist(data, bins=30, edgecolor='black')
ax[0].set_title('Histogram')
ax[0].set_xlabel('Value')
ax[0].set_ylabel('Frequency')

# Density Plot
density = gaussian_kde(data)
xs = np.linspace(min(data), max(data), 200)
ax[1].plot(xs, density(xs), lw=2)
ax[1].fill_between(xs, density(xs), alpha=0.5)
ax[1].set_title('Density Plot')
ax[1].set_xlabel('Value')
ax[1].set_ylabel('Density')

# Show the plots
plt.show()
