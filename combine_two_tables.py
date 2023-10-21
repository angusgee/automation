import pandas as pd
from tabulate import tabulate as tblt

# Create person df
person = pd.DataFrame({
    'personId': [1, 2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bob']
})

# Create address df
address = pd.DataFrame({
    'addressId': [1, 2],
    'personId': [2, 3],
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California']
})

# Set the addressId and personId to int8 to save memory
# Other useful data types for pandas dfs: 
# int8, int16, int32, int64: Signed integers with varying sizes (8, 16, 32, or 64 bits)
# uint8, uint16, uint32, uint64: Unsigned integers (cannot be negative) with varying sizes
# float16, float32, float64: Floating-point numbers with varying precision
# object, bool, string, category (for a small number of unique values)
address['personId'] = address['personId'].astype('int8')
address['addressId'] = address['addressId'].astype('int8')

# Left join the two dfs
# Note the type annotations
def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(person, address, how='left', on='personId')
    df = df[['firstName', 'lastName', 'city', 'state']]
    return df

def main():
    df = (combine_two_tables(person, address))
    print(tblt(df.fillna('Null'), headers='keys', tablefmt='pretty', showindex=False))

if __name__ == '__main__':
    main()
