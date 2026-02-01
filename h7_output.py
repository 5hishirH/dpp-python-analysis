import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dataframe import df

# --- 1. PREPARE DATA ---
# Create a new column to label the groups explicitly
# This makes plotting and grouping much easier
df['Experience_Group'] = df['B7'].apply(lambda x: 'High Experience (>=4)' if x >= 4 else 'Low Experience (<4)')

# Define the variable we are measuring (D2: Ready_Milestones)
timeline_var = 'D2' 

# --- 2. GENERATE TABLE 3 (Group Statistics) ---
# We need Count (N), Mean, and Std Dev
group_stats = df.groupby('Experience_Group')[timeline_var].agg(['count', 'mean', 'std']).reset_index()

# Rename for Academic Presentation
group_stats.columns = ['Group', 'N', 'Mean', 'Std. Deviation']

# Calculate Standard Error Mean (often required for Table 3)
group_stats['Std. Error Mean'] = group_stats['Std. Deviation'] / (group_stats['N'] ** 0.5)

# Export to Excel
output_excel = 'H3_Group_Statistics.xlsx'
group_stats.to_excel(output_excel, index=False)
print(f"Table saved to {output_excel}")

# --- 3. GENERATE FIGURE (Bar Chart with Error Bars) ---
sns.set_style("whitegrid")
plt.figure(figsize=(8, 6))

# Barplot automatically calculates the Mean (height of bar) and 95% Confidence Interval (error bar)
ax = sns.barplot(
    data=df,
    x='Experience_Group',
    y=timeline_var,
    capsize=0.1,             # Adds the little "caps" to the error bars
    palette=['#e02a1f', '#2b7bba'], # Red and Blue colors
    errorbar=('ci', 95)      # Show 95% Confidence Interval
)

plt.title('Comparison of Timeline Definition by Digital Experience', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Digital Transformation Experience', fontsize=12)
plt.ylabel('Defined Timeline Score (D2)', fontsize=12)

# Save the image
output_img = 'H3_Comparison_BarChart.png'
plt.savefig(output_img, dpi=300, bbox_inches='tight')
print(f"Figure saved to {output_img}")

plt.show()