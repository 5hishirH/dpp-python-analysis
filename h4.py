# Hypothesis 04: Regulatory awareness is positively correlated with budget allocation for digital initiatives.

from prep import df

import scipy.stats as stats

# E1: Awareness_regs
# C1: Mgmt_Budget
awareness = df['E1']    # Q15
budget = df['C1']   # Q8

corr, p_value = stats.spearmanr(awareness, budget)

print(f"H8 Correlation Coefficient: {corr:.3f}")
print(f"H8 P-value: {p_value:.5f}")

# INTERPRETATION:
# If p_value < 0.05: The relationship is real (statistically significant).
# If corr is positive (e.g., +0.6): High Awareness = High Budget.
# If corr is near 0: Knowing the rules doesn't make them spend money.
