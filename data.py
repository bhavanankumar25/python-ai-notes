"""import pandas as pd

data = {
    "Name": ["Bhavana", "Priya", "Raj", "Sneha", "Arjun"],
    "Age": [22, 25, 20, 23, 27],
    "Salary": [35000, 50000, 28000, 42000, 60000],
    "City": ["Bangalore", "Mumbai", "Chennai", "Delhi", "Hyderabad"]
}

df = pd.DataFrame(data)
print(df)

 
print(df[df["Age"] > 22])


print(df.sort_values("Salary", ascending=False))


df["Tax"] = df["Salary"] * 0.10
print(df)
"""

import pandas as pd

df = pd.read_csv("ai_job_market_dataset.csv")  # replace with actual filename
print(df.shape)
print(df.columns.tolist())
print(df.head())