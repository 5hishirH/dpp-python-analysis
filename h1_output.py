import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from dataframe import df, readiness_score

# --- CONFIGURATION ---
# Define the groups you are comparing (as per your H1)
groups_to_compare = ['Medium', 'Large']
independent_var = 'Company_Size'
dependent_var = readiness_score

# Filter the dataframe to only include relevant groups and drop missing values
sub_df = df[df[independent_var].isin(groups_to_compare)].dropna(subset=[dependent_var])

# ==========================================
# 1. GENERATE TABLE A: DESCRIPTIVE STATISTICS
# ==========================================
# Group by Company Size and calculate Count (N), Mean, and Standard Deviation
table_a = sub_df.groupby(independent_var)[dependent_var].agg(['count', 'mean', 'std']).reset_index()

# Rename columns to Academic Standards
table_a.columns = ['Group', 'N', 'Mean (M)', 'Std Dev (SD)']

# Add a "Total" row (optional but recommended for Table A)
total_row = pd.DataFrame({
    'Group': ['Total'],
    'N': [len(sub_df)],
    'Mean (M)': [sub_df[dependent_var].mean()],
    'Std Dev (SD)': [sub_df[dependent_var].std()]
})
table_a = pd.concat([table_a, total_row], ignore_index=True)


# ==========================================
# 2. GENERATE TABLE B: ANOVA SUMMARY
# ==========================================
# We use Ordinary Least Squares (OLS) to get the full ANOVA table
# Formula syntax: "Readiness_Score ~ C(Company_Size)"
formula = f'{dependent_var} ~ C({independent_var})'
model = ols(formula, data=sub_df).fit()

# typ=2 is standard for checking main effects
table_b = sm.stats.anova_lm(model, typ=2) 

# Calculate Mean Square (MS) which statsmodels doesn't output by default
# MS = Sum_Squares / Degrees_of_Freedom
table_b['mean_sq'] = table_b['sum_sq'] / table_b['df']

# Reorder and Rename columns to match APA style: Source | SS | df | MS | F | p
# The index contains the Source names (e.g., C(Company_Size) and Residual)
table_b = table_b.reset_index()
table_b = table_b[['index', 'sum_sq', 'df', 'mean_sq', 'F', 'PR(>F)']]

# Clean up column names
table_b.columns = ['Source', 'SS (Sum of Squares)', 'df', 'MS (Mean Square)', 'F', 'p-value']

# Rename the rows for clarity
table_b['Source'] = table_b['Source'].replace({
    f'C({independent_var})': 'Between Groups (Model)',
    'Residual': 'Within Groups (Error)'
})


# ==========================================
# 3. WRITE TO EXCEL
# ==========================================
output_file = 'Academic_ANOVA_Results.xlsx'

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Write Table A
    table_a.to_excel(writer, sheet_name='Table_A_Descriptive', index=False)
    
    # Write Table B
    table_b.to_excel(writer, sheet_name='Table_B_ANOVA_Summary', index=False)
    
    # Optional: Write raw data for reference
    sub_df[[independent_var, dependent_var]].to_excel(writer, sheet_name='Raw_Data', index=False)

print(f"Success! Generated {output_file}")
print("Sheet 1: Descriptive Stats (Mean, SD)")
print("Sheet 2: ANOVA Summary (SS, df, MS, F, p)")