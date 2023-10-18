import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate random date
def random_date(start, end):
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)

# Create test data
data = {
    "date": [random_date(datetime(2021, 1, 1), datetime(2021, 12, 31)) for _ in range(600)],
    "customer_id": [random.randint(1, 1000) for _ in range(600)],
    "sport": [random.choice(["Soccer", "Basketball", "Tennis", "Baseball", "Hockey"]) for _ in range(600)],
    "stake": [random.uniform(1, 1000) for _ in range(600)],
    "odds": [random.uniform(1.0, 10.0) for _ in range(600)],
    "win_y/n": [random.choice(["Y", "N"]) for _ in range(600)],
}

df = pd.DataFrame(data)

# Save test data to three CSV files
df.iloc[:100].to_csv("output20220228.csv", index=False)
df.iloc[200:300].to_csv("output20220307.csv", index=False)
df.iloc[300:].to_csv("output20220314.csv", index=False)