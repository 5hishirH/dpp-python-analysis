import matplotlib.pyplot as plt
import seaborn as sns
from dataframe import df

# --- Configuration ---
# Set the visual style
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# --- Generate the Plot ---
# We use x_jitter and y_jitter because survey data (1-5) often overlaps.
# Jitter spreads the dots slightly so you can see the density.
sns.regplot(
    data=df,
    x='E1',
    y='C1',
    x_jitter=0.2,            # Adds slight noise to X to prevent overlap
    y_jitter=0.2,            # Adds slight noise to Y to prevent overlap
    scatter_kws={'alpha': 0.5, 's': 60, 'color': '#2b7bba'}, # Dot style
    line_kws={'color': '#e02a1f', 'linewidth': 2},           # Regression line style
    ci=95
)

# --- Labeling ---
plt.title('Correlation: Regulatory Awareness vs. Budget Allocation', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Regulatory Awareness (E1)', fontsize=12)
plt.ylabel('Budget Allocation (C1)', fontsize=12)

# Set axis limits to match Likert scale (usually 1-5 or 1-7)
plt.ylim(0.5, 5.5)
plt.xlim(0.5, 5.5)

# --- Save the Output ---
output_file = 'H4_Correlation_Scatterplot.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')

print(f"Figure saved as {output_file}")
plt.show()