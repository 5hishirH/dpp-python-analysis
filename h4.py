# Hypothesis 04: Cost Worry vs Adoption

from dataframe import df, readiness_score
import scipy.stats as stats

# G1: Barrier_Cost

corr_h4, p_h4 = stats.pearsonr(df['G1'], df[readiness_score])
print(f"H4 (Cost vs Ready): Correlation={corr_h4:.2f}, p-value={p_h4:.4f}")