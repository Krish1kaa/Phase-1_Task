import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # Importing matplotlib.pyplot
# Generate a DatetimeIndex with a specified length and time zone
start_date = '2022-01-01'
periods = 10  # Number of periods (days)

# Generate date range with UTC time zone
date_rng_utc = pd.date_range(start=start_date, periods=periods, freq='D', tz='UTC')

# Create a DataFrame with the generated DatetimeIndex and some sample data
df_utc = pd.DataFrame(date_rng_utc, columns=['date'])
df_utc['data'] = np.random.randn(len(date_rng_utc))  # Generating random data

# Localize to a different time zone
df_utc['date'] = df_utc['date'].dt.tz_localize(None).dt.tz_localize('UTC')
df_utc = df_utc.set_index('date')

# Convert to another time zone (e.g., US/Eastern)
df_est = df_utc.tz_convert('US/Eastern')

# Generate another date range with a different time zone (e.g., Europe/London)
date_rng_london = pd.date_range(start=start_date, periods=periods, freq='D', tz='Europe/London')

# Create another DataFrame with the new time zone
df_london = pd.DataFrame(date_rng_london, columns=['date'])
df_london['data'] = np.random.randn(len(date_rng_london))  # Generating random data
df_london = df_london.set_index('date')

# Combine the two DataFrames by aligning their time zones
df_combined = pd.concat([df_est, df_london.tz_convert('US/Eastern')], axis=1, keys=['US/Eastern', 'Europe/London'])

# Display the combined DataFrame
print(df_combined)

# Plotting the time series data
df_combined.plot(figsize=(12, 8), title='Time Series Data in Different Time Zones')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
