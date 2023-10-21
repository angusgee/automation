import pandas as pd
from tabulate import tabulate as tblt

student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

# Create df with a list of integers
# Define the column names as the second argument
def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

def main():
    df = createDataframe(student_data)
    print(tblt(df.fillna('Null'), headers='keys', tablefmt='pretty', showindex=False))

if __name__ == '__main__':
    main()
