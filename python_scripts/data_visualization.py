import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

# Create reports/charts folder if it doesn't exist
charts_dir = "../reports/charts"
os.makedirs(charts_dir, exist_ok=True)

# Load dataset
df = pd.read_csv("../dataset/reviews_cleaned.csv")  # Use cleaned dataset

# Open PDF file to save all charts
pdf_path = "../reports/ecommerce_analysis.pdf"
with PdfPages(pdf_path) as pdf:
    
    # 1. Rating Distribution
    plt.figure(figsize=(8, 5))
    sns.countplot(x=df["rating"], hue=df["rating"], palette="coolwarm", legend=False)
    plt.title("Rating Distribution")
    plt.savefig(f"{charts_dir}/rating_distribution.png")
    pdf.savefig()  # Save to PDF
    plt.close()

    # 2. Number of Reviews per Platform
    plt.figure(figsize=(8, 5))
    sns.countplot(x=df["platform"], hue=df["platform"], palette="Set1", legend=False)
    plt.title("Number of Reviews per Platform")
    plt.savefig(f"{charts_dir}/review_count.png")
    pdf.savefig()  # Save to PDF
    plt.close()

    # 3. Average Rating per Platform
    plt.figure(figsize=(8, 5))
    sns.barplot(x="platform", y="rating", data=df, hue="platform", palette="Set2", legend=False, estimator=lambda x: sum(x) / len(x))
    plt.title("Average Rating per Platform")
    plt.savefig(f"{charts_dir}/average_rating.png")
    pdf.savefig()  # Save to PDF
    plt.close()

    # 4. Platform Distribution
    plt.figure(figsize=(8, 5))
    sns.countplot(x="platform", data=df, hue="platform", palette="Paired", legend=False)
    plt.title("Platform Distribution")
    plt.savefig(f"{charts_dir}/platform_distribution.png")
    pdf.savefig()  # Save to PDF
    plt.close()

print(f"Charts saved in {charts_dir}/ and PDF report saved as {pdf_path}")
