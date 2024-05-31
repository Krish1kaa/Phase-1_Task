import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
np.random.seed(0)  # For reproducibility
categories = ['A', 'B', 'C', 'D', 'E']
data = {
    'Category': np.random.choice(categories, 200),
    'Value': np.random.randn(200) + np.random.rand(200) * 10
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Grouping data by category
grouped_data = [df[df['Category'] == category]['Value'] for category in categories]

# Box Plot
plt.figure(figsize=(12, 8))
plt.boxplot(grouped_data, labels=categories, patch_artist=True)
plt.title('Box Plots of Value by Category')
plt.xlabel('Category')
plt.ylabel('Value')
plt.grid(True)  # Adds a grid for better readability
plt.show()
