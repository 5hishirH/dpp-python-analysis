import matplotlib.pyplot as plt
import seaborn as sns
from dataframe import df, mgmt_support_score, readiness_score

# --- Configuration ---
# Set the visual style for academic publication
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# --- Generate the Plot ---
# sns.regplot creates the scatter plot AND the regression line automatically
# ci=95 adds the 95% confidence interval (the light blue shaded area)
sns.regplot(
    data=df,
    x=mgmt_support_score,
    y=readiness_score,
    scatter_kws={'alpha': 0.6, 's': 70, 'color': '#2b7bba'}, # Style for the dots (transparency, size, color)
    line_kws={'color': '#e02a1f', 'linewidth': 2},           # Style for the regression line (red)
    ci=95
)

# --- Labeling (APA Style) ---
plt.title('Correlation between Top Management Support and DPP Readiness', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Top Management Support Score', fontsize=12)
plt.ylabel('DPP Readiness Score', fontsize=12)

# Set axis limits to make the plot cleaner (optional, adjust based on your data scale 1-5 or 1-7)
# plt.ylim(1, 5.5)
# plt.xlim(1, 5.5)

# --- Save the Output ---
output_file = 'H2_Correlation_Scatterplot.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight') # dpi=300 is standard for print quality

print(f"Plot saved successfully as {output_file}")
plt.show()