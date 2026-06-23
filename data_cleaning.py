import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
print("Program Started")
df = pd.read_csv("sales_data.csv")

print("Original Dataset")
print(df)

# Handle missing values
df["Sales"].fillna(df["Sales"].mean(), inplace=True)
df["Profit"].fillna(df["Profit"].mean(), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove outliers
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df["Sales"] >= lower) &
        (df["Sales"] <= upper)]

# Save cleaned data
df.to_csv("cleaned_sales_data.csv",
          index=False)

print("\nCleaned Dataset")
print(df)

# Visualization 1
plt.figure(figsize=(6,4))
sns.barplot(x="Category",
            y="Sales",
            data=df)
plt.title("Sales by Category")
plt.show()

# Visualization 2
plt.figure(figsize=(6,4))
sns.histplot(df["Sales"],
             bins=5,
             kde=True)
plt.title("Sales Distribution")
plt.show()

# Visualization 3
region_sales = df.groupby("Region")["Sales"].sum()

region_sales.plot(kind="pie",
                  autopct="%1.1f%%")

plt.title("Regional Sales")
plt.ylabel("")
plt.show()

print("Project Completed Successfully")