# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data for product categories and satisfaction scores
np.random.seed(42)
categories = ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Beauty", "Toys"]
satisfaction = [round(np.random.normal(loc=score, scale=0.3, size=50).mean(), 2) 
                for score in [4.2, 3.8, 4.0, 3.5, 4.3, 3.9]]

# Create DataFrame
df = pd.DataFrame({
    "Category": categories,
    "Satisfaction": satisfaction
})

# Create figure (8x8 inches at 64 dpi = 512x512 px)
plt.figure(figsize=(8, 8))

# Create barplot
ax = sns.barplot(
    data=df,
    x="Category",
    y="Satisfaction",
    palette="Blues_d"
)

# Customize chart
ax.set_title("Average Customer Satisfaction by Product Category", fontsize=16, pad=20)
ax.set_xlabel("Product Category", fontsize=14)
ax.set_ylabel("Average Satisfaction Score (1–5)", fontsize=14)
ax.set_ylim(0, 5)

# Rotate x-labels for readability
plt.xticks(rotation=30, ha="right")

# Save chart with exact size (512x512 px)
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
