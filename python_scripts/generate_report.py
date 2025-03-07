import pandas as pd

# Load the dataset
df = pd.read_csv("../dataset/reviews_cleaned.csv")

# Generate summary statistics
summary = df.describe(include="all")

# Count reviews per platform
platform_counts = df["platform"].value_counts()

# Count ratings distribution
rating_counts = df["rating"].value_counts()

# Extract key insights
most_reviews_platform = platform_counts.idxmax()
most_reviews_count = platform_counts.max()
highest_rating = df["rating"].max()
lowest_rating = df["rating"].min()
average_rating = df["rating"].mean()

# Save summary to a text file
summary_text = f"""
📌 **Dataset Overview:**
{df.head().to_string(index=False)}

📊 **Summary Statistics:**
{summary.to_string()}

📌 **Review Count per Platform:**
{platform_counts.to_string()}

📊 **Rating Distribution:**
{rating_counts.to_string()}

🔍 **Key Insights:**
- 📌 Most reviewed platform: {most_reviews_platform} ({most_reviews_count} reviews)
- ⭐ Average Rating: {average_rating:.2f}
- 🔴 Lowest Rating: {lowest_rating}
- 🟢 Highest Rating: {highest_rating}
"""

with open("../reports/summary.txt", "w", encoding="utf-8") as f:
    f.write(summary_text)

print("Summary report saved in reports/summary.txt ✅")
