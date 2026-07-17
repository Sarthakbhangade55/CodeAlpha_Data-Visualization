# 📚 Web Scraping and Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project demonstrates the complete data collection and analysis workflow using Python. It includes web scraping to collect book information from a public website and Exploratory Data Analysis (EDA) to understand the dataset through statistical analysis and visualizations.

The project was completed as part of an internship assignment.

---

## 🎯 Objectives

### Task 1: Web Scraping
- Extract book data from a public website using Python.
- Learn HTML parsing with BeautifulSoup.
- Handle website pagination.
- Create a custom dataset in CSV format.

### Task 2: Exploratory Data Analysis (EDA)
- Ask meaningful questions before analysis.
- Explore the dataset structure and data types.
- Identify trends, patterns, and anomalies.
- Test hypotheses using statistics and visualizations.
- Detect potential data quality issues.

---

## 🛠️ Technologies Used

- Python 3.13
- Requests
- BeautifulSoup4
- Pandas
- Matplotlib
- Seaborn
- LXML

---

## 📂 Website Used

https://books.toscrape.com/

This website is designed for practicing web scraping and is suitable for educational purposes.

---

## 📁 Project Structure

```
Web_Scraping_Internship_Task/
│
├── web_scraper.py
├── data_analysis.py
├── data_visualization.py
├── eda.py
│
├── books_dataset.csv
│
├── rating_distribution.png
├── price_distribution.png
│
├── eda_outputs/
│   ├── books_per_page.png
│   ├── correlation_heatmap.png
│   ├── price_distribution.png
│   ├── price_vs_rating.png
│   └── rating_distribution.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📊 Dataset Information

The dataset contains information collected from 50 pages of the website.

### Features

| Feature | Description |
|----------|-------------|
| Title | Book title |
| Price (£) | Price of the book |
| Availability | Stock availability |
| Rating | Rating converted to values from 1–5 |
| Page | Page number from which the book was scraped |

---

## 🌐 Web Scraping Workflow

1. Send an HTTP request to the website.
2. Download the HTML page.
3. Parse HTML using BeautifulSoup.
4. Extract book details.
5. Navigate through all 50 pages.
6. Store the extracted data in a CSV file.

---

## 📈 Exploratory Data Analysis (EDA)

### Questions Asked

- How many books are available?
- What is the average book price?
- Which book is the most expensive?
- Which book is the least expensive?
- Which rating appears most frequently?
- Are there any missing values?
- Are there duplicate records?
- Is there a relationship between price and rating?
- Are there any outliers in book prices?

---

## 📊 Analysis Performed

- Dataset preview
- Data structure exploration
- Data type inspection
- Missing value detection
- Duplicate record detection
- Summary statistics
- Rating distribution analysis
- Price distribution analysis
- Correlation analysis
- Price vs Rating comparison

---

## 📈 Visualizations

The project generates the following charts:

- Rating Distribution
- Price Distribution
- Price vs Rating (Box Plot)
- Books per Page
- Correlation Heatmap

All charts are stored inside the **eda_outputs** folder.

---

## 📌 Key Findings

- Successfully scraped **1000 books** from **50 pages**.
- Average book price is approximately **£35.07**.
- Book ratings range from **1 to 5**.
- The dataset contains **no missing values**.
- The dataset contains **no duplicate records**.
- Book prices vary across different rating categories.
- The dataset is clean and suitable for further analysis or machine learning.

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the web scraper

```bash
python web_scraper.py
```

### 4. Perform data analysis

```bash
python data_analysis.py
```

### 5. Generate visualizations

```bash
python data_visualization.py
```

### 6. Run Exploratory Data Analysis

```bash
python eda.py
```

---

## 📚 Learning Outcomes

This project demonstrates:

- Python programming
- Web scraping
- HTML parsing
- Website navigation and pagination
- Data cleaning
- CSV dataset creation
- Exploratory Data Analysis (EDA)
- Statistical analysis
- Data visualization
- Working with Pandas, Matplotlib, and Seaborn

---

---

## 📖 Data Story

The visualizations provide meaningful insights into the dataset:

- The **Rating Distribution** chart shows how books are distributed across different rating categories.
- The **Price Distribution** chart highlights the overall spread of book prices.
- The **Price vs Rating** box plot compares book prices across rating groups.
- The **Average Price by Rating** chart summarizes average prices for each rating category.
- The **Top 10 Most Expensive Books** chart identifies premium-priced books.
- The **Books per Page** chart confirms that data was collected consistently across all pages.
- The **Correlation Heatmap** illustrates relationships between numeric variables.
- The **Dashboard** combines key visualizations into a single overview for quick analysis.

These visualizations transform raw data into actionable insights and support data-driven decision-making.

## 📊 Dashboard

![Dashboard](visualizations/dashboard.png)

## 📈 Visualizations

### Rating Distribution

![Rating Distribution](visualizations/chart1_rating_distribution.png)

### Price Distribution

![Price Distribution](visualizations/chart2_price_distribution.png)

### Price vs Rating

![Price vs Rating](visualizations/chart3_price_vs_rating.png)

### Average Price by Rating

![Average Price by Rating](visualizations/chart4_average_price_by_rating.png)

### Top 10 Most Expensive Books

![Top 10 Most Expensive Books](visualizations/chart5_top10_expensive_books.png)

### Books per Page

![Books per Page](visualizations/chart6_books_per_page.png)

### Correlation Heatmap

![Correlation Heatmap](visualizations/chart7_correlation_heatmap.png)

### Rating Pie Chart

![Rating Pie Chart](visualizations/chart8_rating_pie_chart.png)


## 👨‍💻 Author

**Sarthak Bhangade**

B.Tech – Artificial Intelligence & Data Science

---

## 📄 License

This project is developed for educational and internship purposes.


