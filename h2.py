# Having top management support leads to higher readiness.

from dataframe import df, mgmt_support_score, readiness_score
import scipy.stats as stats

corr_h2, p_h2 = stats.pearsonr(df[mgmt_support_score], df[readiness_score])
print(f"H2 (Mgmt vs Ready): Correlation={corr_h2:.2f}, p-value={p_h2:.4f}")