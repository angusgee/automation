import pandas as pd

data = [
    {'name': 'Piper', 'salary': 4548},
    {'name': 'Grace', 'salary': 28150},
    {'name': 'Georgia', 'salary': 1103},
    {'name': 'Willow', 'salary': 6593},
    {'name': 'Finn', 'salary': 74576},
    {'name': 'Thomas', 'salary': 24433}
]

df = pd.DataFrame(data)

# Creat a new column for bonus where the values are the salary doubled
df['bonus'] = df['salary'] * 2

print(df.head())