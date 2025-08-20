import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns

# ---------------------------
# Synthetic business data
# ---------------------------
rng = np.random.default_rng(42)

categories = [
    "Electronics", "Home & Kitchen", "Apparel", "Beauty",
    "Sports", "Grocery", "Toys", "Automotive", "Health", "Office Supplies"
]

# Mean satisfaction (1–5) per category to simulate business reality
means = {
    "Electronics": 4.1,
    "Home & Kitchen": 3.8,
    "Apparel": 3.6,
    "Beauty": 4.0,
    "Sports": 3.7,
    "Grocery": 4.2,
    "Toys": 3.9,
    "Automotive": 3.5,
    "Health": 4.3,
    "Office Supplies": 3.8
}

# Generate realistic per-customer satisfaction observations
rows = []
for cat in categories:
    n = int(rng.integers(120, 260))  # customers per category
    # Normal noise around the mean, clipped to [1, 5]
    vals = np.clip(rng.normal(loc=means[cat], scale=0.35, size=n), 1.0, 5.0)
    for v in vals:
        rows.append((cat, v))

df = pd.DataFrame(rows, columns=["category", "satisfaction"])

# ---------------------------
# Seaborn styling
# ---------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # presentation-ready sizing

# ---------------------------
# Barplot: average satisfaction with 95% CI
# ---------------------------
plt.figure(figsize=(8, 8))  # 8 in * 64 dpi = 512 px
ax = sns.barplot(
    data=df,
    x="category",
    y="satisfaction",
    estimator=np.mean,
    ci=95,                 # 95% CI; for newer seaborn this is deprecated but remains backward-compatible
    palette="crest"
)

ax.set_title("Average Customer Satisfaction by Product Category", pad=14)
ax.set_xlabel("Product Category")
ax.set_ylabel("Average Score (1–5)")
ax.set_ylim(1, 5)
for label in ax.get_xticklabels():
    label.set_rotation(30)
    label.set_ha("right")

# Optional value labels for executive readability
group_means = df.groupby("category")["satisfaction"].mean().reindex(categories)
for idx, p in enumerate(ax.patches):
    height = p.get_height()
    ax.annotate(f"{group_means.iloc[idx]:.2f}",
                (p.get_x() + p.get_width() / 2.0, height),
                ha="center", va="bottom", fontsize=11, xytext=(0, 5), textcoords="offset points")

# ---------------------------
# Export at exactly 512x512
# ---------------------------
# Save with specified dpi and tight layout as requested
plt.savefig("chart.png", dpi=64, bbox_inches="tight")

# Force exact 512x512 in case tight bounding box alters pixel extent
im = Image.open("chart.png").convert("RGBA")
if im.size != (512, 512):
    im = im.resize((512, 512), Image.LANCZOS)
    im.save("chart.png")

print("chart.png written (512x512).")
