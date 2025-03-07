import pandas as pd

# Load dataset
file_path = "../dataset/reviews.csv"  # Update if needed
df = pd.read_csv(file_path)

# Display basic info before cleaning
print("Before Cleaning:")
print(df.info())

# Convert 'date' column to proper datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows where 'date' is still NaT (invalid dates)
df = df.dropna(subset=['date'])

# Remove duplicate reviews (if any)
df = df.drop_duplicates()

# Save cleaned dataset
cleaned_file_path = "../dataset/reviews_cleaned.csv"
df.to_csv(cleaned_file_path, index=False)

# Display basic info after cleaning
print("After Cleaning:")
print(df.info())
print("Cleaned dataset saved successfully!")
