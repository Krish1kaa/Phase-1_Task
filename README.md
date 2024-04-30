# Task 1A
## [i] Data Cleaning with Pandas

This Python script demonstrates basic data cleaning techniques using the Pandas library. It includes:

1. Identifying missing data (`NaN`) in a DataFrame.
2. Converting non-numeric values to numeric using `pd.to_numeric`.
3. Filling missing values with the mean of each column.
4. Identifying and removing duplicate rows in a DataFrame.

## Requirements

- Python 3.x
- Pandas
- NumPy

## Usage

1. Install the required libraries if you haven't already:

   ```bash
   pip install pandas numpy
## Example
Consider the following DataFrame df:
|   | A   | B   | C   |
|---|-----|-----|-----|
| 0 | 1   | a   | 1   |
| 1 | 2   | b   | 2   |
| 2 | NaN | c   | 3   |
| 3 | 4   | d   | 4   |
| 4 | 5   | e   | 5   |
Missing Data:
The script identifies missing data in df:
|   | A      | B      | C      |
|---|--------|--------|--------|
| 0 | False  | False  | False  |
| 1 | False  | False  | False  |
| 2 | True   | False  | False  |
| 3 | False  | False  | False  |
| 4 | False  | False  | False  |
Filling Missing Data:
Non-numeric values are converted to NaN and missing values are filled with the mean of each column:
|   | A     | B     | C     |
|---|-------|-------|-------|
| 0 | 1.0   | NaN   | 1.0   |
| 1 | 2.0   | NaN   | 2.0   |
| 2 | 3.0   | NaN   | 3.0   |
| 3 | 4.0   | NaN   | 4.0   |
| 4 | 5.0   | NaN   | 5.0   |
Duplicate Rows:
Duplicate rows are identified and removed:
Duplicate Rows:
|   | Duplicate |
|---|-----------|
| 0 | False     |
| 1 | False     |
| 2 | False     |
| 3 | False     |
| 4 | False     |

Deduplicated Data:
|   | A | B | C |
|---|---|---|---|
| 0 | 1 | a | 1 |
| 1 | 2 | b | 2 |
| 2 | 3 | c | 3 |
| 3 | 4 | d | 4 |
| 4 | 5 | e | 5 |
## [ii] Hierarchical Indexing in Pandas

This Python script demonstrates hierarchical indexing in Pandas, creating a Series with hierarchical indexing and selecting subsets of data at outer and inner levels using partial indexing.

## Requirements

- Python 3.x
- Pandas

## Usage

1. Install Pandas if you haven't already:

   ```bash
   pip install pandas
## Example
Consider the following Series series with hierarchical indexing:
|   |   |   |
|---|---|---|
| A | 1 | 1 |
|   | 2 | 2 |
|   | 3 | 3 |
| B | 1 | 4 |
|   | 2 | 5 |
|   | 3 | 6 |

Selecting Subsets of Data
The script demonstrates selecting subsets of data at outer and inner levels using partial indexing:
Selecting data at the outer level 'A':

|   |   |
|---|---|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
Selecting data at the inner level 2:
|   |   |
|---|---|
| A | 2 |
| B | 5 |
# Task 1B
## [i] Plotting Trigonometric Functions

This Python script demonstrates how to plot trigonometric functions using Matplotlib. It creates subplots for sine and cosine functions, annotates maximum and minimum points, and customizes the plot appearance.

## Requirements

- Python 3.x
- Matplotlib
- NumPy

## Usage

1. Install Matplotlib and NumPy if you haven't already:

   ```bash
   pip install matplotlib numpy
## Example
The script creates a figure with two subplots, one for the sine function and the other for the cosine function. It annotates the maximum and minimum points on each subplot and customizes the plot appearance.

## Plot
<img width="498" alt="Screenshot 2024-04-30 214451" src="https://github.com/Krish1kaa/SKDSI-112_Phase-1_Task/assets/150791638/5ce4089b-c025-4403-9646-d119857e4058">

## [ii] [a] Bar Plot with Pandas DataFrame

This Python script demonstrates how to create a bar plot using a Pandas DataFrame. It creates a sample DataFrame and then plots the data as a bar chart.

## Requirements

- Python 3.x
- Pandas
- Matplotlib

## Usage

1. Install Pandas and Matplotlib if you haven't already:

   ```bash
   pip install pandas matplotlib

## Example
The script creates a bar plot using a sample DataFrame df:

|    | A   | B   | C   |
|----|-----|-----|-----|
| X  | 10  | 15  | 20  |
| Y  | 20  | 25  | 30  |
| Z  | 30  | 35  | 40  |
| W  | 40  | 45  | 50  |
## Bar Plot
<img width="486" alt="Screenshot 2024-04-30 215200" src="https://github.com/Krish1kaa/SKDSI-112_Phase-1_Task/assets/150791638/aa317f34-4fed-4fd4-929c-7cbbace95579">

## [ii] [b] Bar Plot and Stacked Bar Plot with Pandas DataFrame

This Python script demonstrates how to create a bar plot and a stacked bar plot using a Pandas DataFrame. It creates a sample DataFrame and then plots the data as bar charts.

## Requirements

- Python 3.x
- Pandas
- Matplotlib

## Usage

1. Install Pandas and Matplotlib if you haven't already:

   ```bash
   pip install pandas matplotlib
## Example
The script creates a bar plot and a stacked bar plot using a sample DataFrame df:
|    | A   | B   | C   |
|----|-----|-----|-----|
| X  | 10  | 15  | 20  |
| Y  | 20  | 25  | 30  |
| Z  | 30  | 35  | 40  |
| W  | 40  | 45  | 50  |
## Bar Plot
The first plot shows the values of columns 'A', 'B', and 'C' for indices 'X', 'Y', 'Z', and 'W' as individual bars.
## Stacked Bar Plot
The second plot shows the values of columns 'A', 'B', and 'C' for indices 'X', 'Y', 'Z', and 'W' as stacked bars.
<img width="474" alt="Screenshot 2024-04-30 215433" src="https://github.com/Krish1kaa/SKDSI-112_Phase-1_Task/assets/150791638/7ead9362-51b1-4b73-9e2b-cb40a5ad11dc">




