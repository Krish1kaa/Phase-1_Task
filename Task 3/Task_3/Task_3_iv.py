import pandas as pd
import matplotlib.pyplot as plt  # Importing matplotlib.pyplot
# Create a period object
period = pd.Period('2022-01', freq='M')

# Perform period arithmetic
period_plus_3 = period + 3  # Adding 3 months
period_minus_2 = period - 2  # Subtracting 2 months

print("Original Period:", period)
print("Period + 3 months:", period_plus_3)
print("Period - 2 months:", period_minus_2)

# Construct a range of periods using period_range
period_range = pd.period_range(start='2022-01', end='2022-12', freq='M')

print("\nRange of Periods:")
print(period_range)

# Convert to DataFrame and display
df = pd.DataFrame({'Period': period_range})
print("\nDataFrame with Periods:")
print(df)

# Plotting the periods
df['Value'] = range(len(df))  # Adding some sample data for plotting
df.set_index('Period').plot(figsize=(10, 6), title='Range of Periods')
plt.xlabel('Period')
plt.ylabel('Value')
plt.show()
