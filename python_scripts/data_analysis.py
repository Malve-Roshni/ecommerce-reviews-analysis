import pandas as pd

# Read the cleaned data
file_path = "../dataset/reviews_cleaned.csv"
file_path = r"C:\Users\Malve Roshni\Desktop\ecommerce-reviews-analysis\dataset\reviews_cleaned.csv"
df = pd.read_csv(file_path)


# Show first few rows
print("Dataset Overview:")
print(df.head())

# Show summary of the data
print("\nSummary Statistics:")
print(df.describe(include="all"))

# Count of reviews for each platform
print("\nReview Count per Platform:")
print(df['platform'].value_counts())

# Count of each rating
print("\nRating Distribution:")
print(df['rating'].value_counts())

# Save the summary in a text file
summary_path = "../reports/summary.txt"
with open(summary_path, "w") as f:
    f.write("Dataset Overview:\n")
    f.write(str(df.head()) + "\n\n")

    f.write("Summary Statistics:\n")
    f.write(str(df.describe(include='all')) + "\n\n")

    f.write("Review Count per Platform:\n")
    f.write(str(df['platform'].value_counts()) + "\n\n")

    f.write("Rating Distribution:\n")
    f.write(str(df['rating'].value_counts()) + "\n\n")

print(f"Summary saved to {summary_path}")
