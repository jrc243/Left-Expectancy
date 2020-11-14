#1
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

#2
df=pd.read_csv("all_data.csv")
#print(df.head(5))

#3
df.rename(columns={"Life expectancy at birth (years)": "LEABY"}, inplace=True)

#4
print(df.head())

#5
f, ax = plt.subplots(figsize=(15, 10))
sns.barplot(data=df, x="Country", y="GDP")
#plt.show()

#6f, ax = plt.subplots(figsize=(15, 10))
sns.barplot(data=df, x="Country", y="LEABY")
#plt.show()

#7
fig = plt.subplots(figsize=(15, 10))
sns.violinplot(data=df, x="Country", y="LEABY")
#plt.show()

#8
f, ax = plt.subplots(figsize=(15, 10))
ax=sns.barplot(data=df, x="Country", y="GDP", hue="Year")
plt.xticks(rotation="90")
plt.ylabel("GDP in Trillions of U.S. Dollars")
#plt.show()

#9
f, ax = plt.subplots(figsize=(15, 10))
ax=sns.barplot(data=df, x="Country", y="LEABY", hue="Year")
plt.xticks(rotation="90")
plt.ylabel("Life expectancy at birth in years")
#plt.show()

#10 Scatter Plot
g = sns.FacetGrid(df, col="Year", hue="Country", col_wrap=4, height=2)
g = g.map(plt.scatter, "GDP", "LEABY", edgecolor="w").add_legend()
plt.title("GDP in Trillions of U.S. Dollars")
#plt.show()

#11 Plot a line
g3 = sns.FacetGrid(df, col="Country", col_wrap=2, height=4)
g3 = (g3.map(plt.plot, "Year", "LEABY").add_legend())
plt.show()
