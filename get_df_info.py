import pandas as pd

data = [
    {'player_id': 846, 'name': 'Mason', 'age': 21, 'position': 'Forward', 'team': 'RealMadrid'},
    {'player_id': 749, 'name': 'Riley', 'age': 30, 'position': 'Winger', 'team': 'Barcelona'},
    {'player_id': 155, 'name': 'Bob', 'age': 28, 'position': 'Striker', 'team': 'ManchesterUnited'},
    {'player_id': 583, 'name': 'Isabella', 'age': 32, 'position': 'Goalkeeper', 'team': 'Liverpool'},
    {'player_id': 388, 'name': 'Zachary', 'age': 24, 'position': 'Midfielder', 'team': 'BayernMunich'},
    {'player_id': 883, 'name': 'Ava', 'age': 23, 'position': 'Defender', 'team': 'Chelsea'},
    {'player_id': 355, 'name': 'Violet', 'age': 18, 'position': 'Striker', 'team': 'Juventus'},
    {'player_id': 247, 'name': 'Thomas', 'age': 27, 'position': 'Striker', 'team': 'ParisSaint-Germain'},
    {'player_id': 761, 'name': 'Jack', 'age': 33, 'position': 'Midfielder', 'team': 'ManchesterCity'},
    {'player_id': 642, 'name': 'Charlie', 'age': 36, 'position': 'Center-back', 'team': 'Arsenal'}
]

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Print the shape attribute of the df -> (rows, columns)
# The attribute returns a tuple so convert it into a list
print(list(df.shape))

# Print the first n rows of the df
print(df.head(3))

# Print the size of the df, meaning the number of cells -> int
print(df.size)

# Print the data types of each column
print(df.dtypes)

# Print the column headers
print(df.columns)

# Print row labels
print(df.index)

# Return the data as a Numpy array
print(df.values)

# Call a summary of the df
print(df.info())

# Check if the df is empty
print(df.empty)

# Print summary statistics
print(df.describe())

# Print the last n rows of a df
print(df.tail(5))

# Print a sample of n rows
print(df.sample(5))

# Print the number of unique rows in the df
print(df.nunique())

# Sort the df by a particulr column
print(df.sort_values('name'))

# Remove specified columns from the df
df.drop(['name'], axis=1, inplace=True)

# Replace any na/NaN values with the first argument
df.fillna(0, inplace=True)

# Print the mean of all columns
print(df.mean())

# Print the max value in each column
print(df.max())

# Print the min value in each column
print(df.min())
