import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from dataframe import df

# --- 1. RUN REGRESSION RECAP ---
X = df['F3']
Y = df['Readiness_Score']
X_with_const = sm.add_constant(X)
model = sm.OLS(Y, X_with_const).fit()

# --- 2. GENERATE TABLE (Excel) ---
# Create a clean summary table
results_summary = pd.DataFrame({
    'Variable': ['Constant', 'Partner Readiness (F3)'],
    'Coefficient': model.params.values,
    'Std. Error': model.bse.values,
    't-statistic': model.tvalues.values,
    'p-value': model.pvalues.values,
    'R-Squared': [model.rsquared, model.rsquared] # Repeated just to fit the dataframe shape
})

# Rounding
results_summary = results_summary.round(4)

# Save
output_excel = 'H7_Regression_Results.xlsx'
results_summary.to_excel(output_excel, index=False)
print(f"Table saved to {output_excel}")

# --- 3. GENERATE FIGURE (Scatter Plot) ---
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# Plot data points and regression line
sns.regplot(
    x=X, 
    y=Y, 
    scatter_kws={'alpha': 0.6, 'color': '#2b7bba'}, # Blue dots
    line_kws={'color': '#e02a1f', 'linewidth': 2},  # Red line
    ci=95
)

# Add R-squared annotation to the graph
plt.text(
    x=X.min(), 
    y=Y.max(), 
    s=f'$R^2 = {model.rsquared:.2f}$', 
    fontsize=12, 
    bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray')
)

plt.title('Impact of Supply Chain Partner Readiness on Org Readiness', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Partner Readiness Score (F3)', fontsize=12)
plt.ylabel('Organizational Readiness Score', fontsize=12)

# Save image
output_img = 'H7_Regression_Plot.png'
plt.savefig(output_img, dpi=300, bbox_inches='tight')
print(f"Figure saved to {output_img}")

plt.show()