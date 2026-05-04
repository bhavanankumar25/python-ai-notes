import pandas as pd

df = pd.read_csv("ai_job_market_dataset.csv")
print(df.shape)
"""
print(df.columns.tolist())
print(df.head())

print(df["Job_Title"].unique())

print(df.groupby("Job_Title")["Salary_USD"].mean().sort_values(ascending=False))

india = df[df["Country"] == "India"]
print(india.shape)
print(india["Job_Title"].value_counts())

print(df["Top_Skill"].value_counts())



india_ai = df[(df["Country"] == "India") & (df["Job_Title"] == "AI Engineer")]
print("Average AI Engineer salary in India: $" + str(round(india_ai["Salary_USD"].mean(), 2)))
print("Max salary: $" + str(india_ai["Salary_USD"].max()))
print("Min salary: $" + str(india_ai["Salary_USD"].min()))
"""


import matplotlib.pyplot as plt


"""avg_salary = df.groupby("Job_Title")["Salary_USD"].mean().sort_values(ascending=False)

avg_salary.plot(kind="bar", color="steelblue")
plt.title("Average Salary by Job Title")
plt.xlabel("Job Title")
plt.ylabel("Salary in USD")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


df["Top_Skill"].value_counts().plot(kind="bar", color="coral")
plt.title("Most In-Demand AI Skills")
plt.xlabel("Skill")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
"""
df["Remote"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Remote vs Non-Remote AI Jobs")
plt.show()
