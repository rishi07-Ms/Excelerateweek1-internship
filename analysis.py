import pandas as pd

# Excel file read
df = pd.read_excel("#DePaul_Data.xlsx")

print("Rows, Columns:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Completely empty columns
empty_cols = df.columns[df.isnull().all()]

print("\nCompletely Empty Columns:")
print(list(empty_cols))

# Remove them
df = df.drop(columns=empty_cols)

print("\nNew Shape:")
print(df.shape)

# Save cleaned dataset
df.to_excel("DePaul_Cleaned.xlsx", index=False)

print("Cleaned dataset saved successfully!")

print("\nRemaining Columns After Cleaning:")
print(df.columns.tolist())

#Top 10 Countries Chart
import matplotlib.pyplot as plt

df['Country'].value_counts().head(10).plot(kind='bar')

plt.title('Top 10 Countries')
plt.xlabel('Country')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

#Top 10 Universities Chart
df['University'].value_counts().head(10).plot(kind='bar')

plt.title('Top 10 Universities')
plt.xlabel('University')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

#Application Source Pie Chart
df['Application_Source'].value_counts().head(5).plot(kind='pie', autopct='%1.1f%%')

plt.title('Application Sources')
plt.ylabel('')
plt.show()

#Attempts Histogram
import matplotlib.pyplot as plt

df['Attempts'].dropna().hist()

plt.title('Attempts Distribution')
plt.xlabel('Attempts')
plt.ylabel('Frequency')
plt.show()


