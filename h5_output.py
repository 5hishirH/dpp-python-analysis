import seaborn as sns
import matplotlib.pyplot as plt
from prep import df

# --- 1. SETUP DATA ---
# precise mapping based on Section 7 of your survey
barrier_names = {
    'G1': 'Cost of Implementation (Q25)',
    'G2': 'Lack of Industry Standards (Q26)',
    'G3': 'Interoperability Issues (Q27)',
    'G4': 'Lack of Skilled Personnel (Q28)',
    'G5': 'Regulatory Uncertainty (Q29)'
}

# Select columns and calculate means
barriers = df[['G1', 'G2', 'G3', 'G4', 'G5']]
barrier_means = barriers.mean().sort_values(ascending=False).reset_index()
barrier_means.columns = ['Code', 'Mean_Score']

# Map the codes to real names for the display
barrier_means['Barrier_Name'] = barrier_means['Code'].map(barrier_names)

# --- 2. GENERATE TABLE 4 (Excel) ---
output_excel = 'H5_Barrier_Ranking.xlsx'
barrier_means[['Barrier_Name', 'Mean_Score']].to_excel(output_excel, index=False)
print(f"Table saved to {output_excel}")

# --- 3. GENERATE FIGURE (Horizontal Bar Chart) ---
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

ax = sns.barplot(
    data=barrier_means,
    x='Mean_Score',
    y='Barrier_Name',
    palette='viridis' 
)

# Add the specific numbers to the end of the bars
for i in ax.containers:
    ax.bar_label(i, fmt='%.2f', padding=5)

plt.title('Ranking of Barriers to DPP Adoption', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Mean Significance Score (1=Strongly Disagree, 5=Strongly Agree)', fontsize=12)
plt.ylabel('Barrier Type', fontsize=12)
plt.xlim(0, 5) 

# Save image
output_img = 'H5_Barrier_Ranking_Plot.png'
plt.savefig(output_img, dpi=300, bbox_inches='tight')
print(f"Figure saved to {output_img}")

plt.show()