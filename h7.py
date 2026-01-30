# Digital experience vs timeline

from dataframe import df
import scipy.stats as stats

# D2: Ready_Milestones
# B7: Digital_Exp

high_exp = df[df['B7'] >= 4]['D2']
low_exp = df[df['B7'] < 4]['D2']

# T-Test
t_stat, p_val = stats.ttest_ind(high_exp, low_exp)
print(f"H7 (Exp vs Timeline): T-stat={t_stat:.2f}, p-value={p_val:.4f}")