import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # Importing matplotlib.pyplot

# Generating a date range
date_rng = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')

# Creating a DataFrame with the date range and some sample data
df = pd.DataFrame(date_rng, columns=['date'])
df['data'] = np.random.randn(len(date_rng))  # Generating random data
df = df.set_index('date')  # Setting the date column as the index

# Display the first few rows of the DataFrame
print(df.head())

# Plotting the time series data
df.plot(figsize=(10, 6), title='Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
