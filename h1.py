# Hypothesis 01: •	Large companies are more ready for DPP than small companies.

from dataframe import df
import scipy.stats as stats

# print(df["Company_Name"].head()) # check unique values in company size

# small = df[df['Company_Size'] == 'Small']['Readiness_Score']
medium = df[df['Company_Size'] == 'Medium']['Readiness_Score']
large = df[df['Company_Size'] == 'Large']['Readiness_Score']

# ANOVA (Analysis of Variance)
f_stat, p_value = stats.f_oneway(medium, large)

print(f"H1 ANOVA Result: F-stat={f_stat:.2f}, p-value={p_value:.4f}")
if p_value < 0.05:
    print("Result: Significant! Size matters.")
else:
    print("Result: Not significant.")
