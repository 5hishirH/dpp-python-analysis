import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from prep import df

# --- 1. RUN THE REGRESSION ---
X = df[['D3', 'D2']]  # D3=Consumer, D2=Gov
Y = df['Readiness_Score']
X = sm.add_constant(X) # Adds the intercept

model = sm.OLS(Y, X).fit()

# --- 2. GENERATE TABLE 5 (Excel) ---
# Extract the data from the model summary
# We need: Coef, Std Err, t, P>|t|, [0.025, 0.975]
results_summary = pd.DataFrame({
    'Variable': ['Constant', 'Consumer Demand (D3)', 'Govt Support (D2)'],
    'Coefficient (B)': model.params.values,
    'Std. Error': model.bse.values,
    't-statistic': model.tvalues.values,
    'p-value': model.pvalues.values,
    'CI Lower (95%)': model.conf_int()[0].values,
    'CI Upper (95%)': model.conf_int()[1].values
})

# Round for cleaner Excel output
results_summary = results_summary.round(4)

output_excel = 'H6_Regression_Results.xlsx'
results_summary.to_excel(output_excel, index=False)
print(f"Regression Table saved to {output_excel}")

# --- 3. GENERATE FIGURE (Coefficient Plot) ---
# We exclude the 'Constant' from the plot because it skews the scale
plot_data = results_summary[results_summary['Variable'] != 'Constant']

plt.figure(figsize=(8, 5))

# Plot the points (Coefficients) and Error Bars (Confidence Intervals)
# yerr is calculated as: Coefficient - Lower_CI (or Upper_CI - Coefficient)
errors = plot_data['Coefficient (B)'] - plot_data['CI Lower (95%)']

plt.errorbar(
    x=plot_data['Variable'], 
    y=plot_data['Coefficient (B)'], 
    yerr=errors, 
    fmt='o',        # 'o' means plot as dots
    color='black',  # Color of dots/lines
    capsize=5,      # Width of the little caps on error bars
    linewidth=2,
    markersize=8
)

# Add a reference line at 0 (if interval crosses 0, it's not significant)
plt.axhline(y=0, color='gray', linestyle='--', linewidth=1)

plt.title('Comparison of Regression Coefficients (Influence Strength)', fontsize=12, fontweight='bold', pad=15)
plt.ylabel('Impact on Readiness (Coefficient)', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate the values next to the dots
for i, txt in enumerate(plot_data['Coefficient (B)']):
    plt.annotate(f"{txt:.3f}", (i, txt), xytext=(10, 0), textcoords='offset points')

output_img = 'H6_Coefficient_Plot.png'
plt.savefig(output_img, dpi=300, bbox_inches='tight')
print(f"Figure saved to {output_img}")

plt.show()