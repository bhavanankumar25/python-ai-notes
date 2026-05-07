import pandas as pd

df = pd.read_csv("ai_job_market_dataset.csv")
print(df.shape)

"""print(df.columns.tolist())
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

"""
import matplotlib.pyplot as plt


avg_salary = df.groupby("Job_Title")["Salary_USD"].mean().sort_values(ascending=False)

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

df["Remote"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Remote vs Non-Remote AI Jobs")
plt.show()"""



from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

le = LabelEncoder()
df['Experience_Code'] = le.fit_transform(df['Experience_Level'])
df['Remote_Code'] = le.fit_transform(df['Remote'])

X = df[['Experience_Code', 'Remote_Code']]
y = df['Salary_USD']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print("Model accuracy score: " + str(round(score * 100, 2)) + "%")

prediction = model.predict([[2, 1]])
print("Predicted salary: $" + str(round(prediction[0], 2)))

# Junior, non-remote
print(model.predict([[0, 0]])[0])

# Mid level, remote
print(model.predict([[1, 1]])[0])

# Senior, remote
print(model.predict([[2, 1]])[0])