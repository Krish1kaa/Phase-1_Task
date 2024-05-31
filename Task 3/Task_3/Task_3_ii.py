import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # Importing matplotlib.pyplot
# Generate a DatetimeIndex with a specified length
start_date = '2022-01-01'
periods = 365  # Number of periods (days)

date_rng = pd.date_range(start=start_date, periods=periods, freq='D')

# Create a DataFrame with the generated DatetimeIndex and some sample data
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
