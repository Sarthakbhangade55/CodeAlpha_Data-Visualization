import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("books_dataset.csv")

# Create output folder
os.makedirs("visualizations", exist_ok=True)

# Better plot style
sns.set_theme(style="whitegrid")

print("=" * 60)
print("TASK 3 : DATA VISUALIZATION")
print("=" * 60)



plt.figure(figsize=(8,5))

sns.countplot(data=df, x="Rating")

plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig("visualizations/chart1_rating_distribution.png")

plt.close()


plt.figure(figsize=(8,5))

sns.histplot(
    df["Price (£)"],
    bins=20,
    kde=True
)

plt.title("Distribution of Book Prices")

plt.xlabel("Price (£)")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("visualizations/chart2_price_distribution.png")

plt.close()



plt.figure(figsize=(8,5))

sns.boxplot(data=df, x="Rating", y="Price (£)")

plt.title("Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")

plt.tight_layout()

plt.savefig("visualizations/chart3_price_vs_rating.png")

plt.close()



avg_price = df.groupby("Rating")["Price (£)"].mean()

plt.figure(figsize=(8,5))

avg_price.plot(kind="bar")

plt.title("Average Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")

plt.tight_layout()

plt.savefig("visualizations/chart4_average_price_by_rating.png")

plt.close()


top_books = df.nlargest(10, "Price (£)")

plt.figure(figsize=(10,6))

plt.barh(top_books["Title"], top_books["Price (£)"])

plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")

plt.tight_layout()

plt.savefig("visualizations/chart5_top10_expensive_books.png")

plt.close()


plt.figure(figsize=(12,5))

sns.countplot(data=df, x="Page")

plt.title("Books Scraped Per Page")
plt.xlabel("Page")
plt.ylabel("Books")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("visualizations/chart6_books_per_page.png")

plt.close()


plt.figure(figsize=(6,4))

sns.heatmap(
    df[["Price (£)", "Rating", "Page"]].corr(),
    annot=True,
    cmap="Blues"
)

plt.title("Correlation Between Numeric Variables")

plt.tight_layout()

plt.savefig("visualizations/chart7_correlation_heatmap.png")

plt.close()


rating_counts = df["Rating"].value_counts().sort_index()

plt.figure(figsize=(6,6))

plt.pie(
    rating_counts,
    labels=rating_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Percentage of Books by Rating")

plt.savefig("visualizations/chart8_rating_pie_chart.png")

plt.close()



print("\nAll visualizations created successfully!")
print("Saved in the 'visualizations' folder.")



# ==========================================
# Dashboard
# ==========================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# ----------------------------
# Chart 1: Rating Distribution
# ----------------------------
sns.countplot(data=df, x="Rating", ax=axes[0, 0])
axes[0, 0].set_title("Rating Distribution")

# ----------------------------
# Chart 2: Price Distribution
# ----------------------------
sns.histplot(df["Price (£)"], bins=20, kde=True, ax=axes[0, 1])
axes[0, 1].set_title("Price Distribution")

# ----------------------------
# Chart 3: Average Price by Rating
# ----------------------------
avg_price = df.groupby("Rating")["Price (£)"].mean()

axes[1, 0].bar(avg_price.index.astype(str), avg_price.values)
axes[1, 0].set_title("Average Price by Rating")
axes[1, 0].set_xlabel("Rating")
axes[1, 0].set_ylabel("Average Price (£)")

# ----------------------------
# Chart 4: Correlation Heatmap
# ----------------------------
sns.heatmap(
    df[["Price (£)", "Rating", "Page"]].corr(),
    annot=True,
    cmap="Blues",
    ax=axes[1, 1]
)

axes[1, 1].set_title("Correlation Heatmap")

plt.suptitle(
    "Books Dataset Dashboard",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

plt.savefig(
    "visualizations/dashboard.png",
    dpi=300
)

plt.close()

print("Dashboard created successfully!")