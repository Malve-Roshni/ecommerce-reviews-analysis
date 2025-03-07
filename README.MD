🛒 E-Commerce Reviews Analysis using Python
📌 Project Overview
This project analyzes customer reviews and ratings for BlinkIt, Zepto, and JioMart to extract insights into customer sentiment, ratings, and platform performance.

Using Python (Pandas, NumPy, Seaborn, Matplotlib), the project examines trends in review counts, rating distributions, sentiment analysis, and platform comparisons to uncover key patterns in e-commerce customer feedback.  

Ecommerce_Reviews_Analysis/
│── dataset/                  # 📁 Contains raw and cleaned customer reviews data
│   ├── reviews.csv           # 📌 Original dataset
│   ├── reviews_cleaned.csv   # ✅ Cleaned dataset (generated after preprocessing)
│
│── python_scripts/           # 📂 Python scripts for data processing and analysis
│   ├── data_cleaning.py       # 🧼 Cleans and preprocesses the dataset
│   ├── data_analysis.py       # 📊 Performs exploratory data analysis (EDA)
│   ├── data_visualization.py  # 📉 Generates charts and visualizations
│   ├── sentiment_analysis.py  # 📝 Performs sentiment analysis on reviews
│   ├── generate_report.py     # 📄 Compiles insights into a PDF report
│
│── reports/                  # 📂 Stores generated reports and insights
│   ├── charts/               # 📊 Contains visualizations from analysis
│   ├── summary.txt           # 📌 Key insights from the analysis
│   ├── ecommerce_analysis.pdf # 📄 Comprehensive project report
│
│── requirements.txt          # 📜 Required Python libraries
│── README.md                 # 📖 Project documentation 

⚙️ Setup & Installation
1️⃣ Install Dependencies
Ensure you have Python installed, then run:

pip install -r requirements.txt
2️⃣ Download or Prepare Dataset
📂 Place the raw dataset (reviews.csv) inside the dataset/ folder.
📌 If you don’t have a dataset, you can collect e-commerce reviews from APIs or web scraping.

3️⃣ Run Data Cleaning
python python_scripts/data_cleaning.py
✅ This will clean and preprocess the data, saving the cleaned version as reviews_cleaned.csv.

4️⃣ Perform Data Analysis
python python_scripts/data_analysis.py
✅ This script performs EDA (Exploratory Data Analysis) and extracts key patterns from customer reviews.

5️⃣ Generate Visualizations
python python_scripts/data_visualization.py
✅ Graphs and visualizations will be saved in the reports/charts/ folder.

6️⃣ Run Sentiment Analysis
python python_scripts/sentiment_analysis.py
✅ This will analyze positive, neutral, and negative sentiments in customer reviews.

7️⃣ Generate PDF Report
python python_scripts/generate_report.py
✅ A final report (ecommerce_analysis.pdf) will be saved inside the reports/ folder.

🔍 Key Insights from Analysis
📊 Sentiment Trends → Proportion of positive, neutral, and negative reviews.
⭐ Rating Distribution → Understanding how customers rate each platform.
📦 Platform Comparisons → Analyzing which platform receives better customer feedback.
🚚 Delivery Experience Feedback → Examining customer complaints & satisfaction levels.

🛠️ Technologies Used
🔹 Python → Pandas, NumPy, Seaborn, Matplotlib, NLP (Natural Language Processing)
🔹 VS Code / Jupyter Notebook → Development environment
🔹 GitHub → Version control

🚀 Usage Instructions
1️⃣ Clone the Repository
git clone https://github.com/malve-Roshni/ecommerce-reviews-analysis.git
cd Ecommerce_Reviews_Analysis

2️⃣ Install Required Libraries
pip install -r requirements.txt

3️⃣ Run Data Cleaning & Analysis
python python_scripts/data_cleaning.py
python python_scripts/data_analysis.py

4️⃣ Generate Visualizations & Insights
python python_scripts/data_visualization.py
python python_scripts/sentiment_analysis.py
python python_scripts/generate_report.py
✅ Visualizations and reports will be saved in the reports/ folder.

📄 About
🛒 E-Commerce Reviews Analysis using Python is a data-driven project that extracts insights from customer feedback on BlinkIt, Zepto, and JioMart. It includes sentiment analysis, rating distribution, and platform performance evaluation with Python scripts, visualizations, and detailed reports.

git clone https://github.com/malve-Roshni/ecommerce-reviews-analysis.git
📌 GitHub Repository: E-Commerce [Reviews Analysis] 