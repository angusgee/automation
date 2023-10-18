import pandas as pd
from datetime import datetime, timedelta

def read_file(read_file):
    return pd.read_csv(read_file)

def remove_rows(df, column, value):
    return df[df[column] != value]

def filter_rows(df, column, value):
    return df[df[column] == value]

def sort_columns(df, *column_orders):
    columns, ascending = zip(*column_orders)
    return df.sort_values(by=list(columns), ascending=ascending)

def increment_date(start_date, date_format, increment):
    start = datetime.strptime(start_date, date_format)
    return start + timedelta(days=increment)

def export_csv(df, filename, date):
    df.to_csv(f'{filename}_{date}.csv', index=False)
    print(f'output successful: {filename}_{date}.csv')

def merge(left_filename, right_filename):
    df_old = pd.read_csv(left_filename)
    df_new = pd.read_csv(right_filename)
    return pd.concat([df_old, df_new], axis=0)
    
def main():
    print('CSV and Pandas Utils by angusg')

if __name__ == '__main__':
    main()