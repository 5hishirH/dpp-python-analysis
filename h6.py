# Hypothesis 7: Organizational readiness is positively moderated by the readiness of supply chain partners.

from dataframe import df
import statsmodels.api as sm
import pandas as pd

# 1. Define your variables
# Y = The calculated average of all Readiness questions (Q18-Q24)
Y = df['Readiness_Score'] 

# X = The specific question about partners (Q20)
X = df['F3'] 

# 2. Run Linear Regression
# Add a constant (intercept) because regression needs a starting point
X = sm.add_constant(X) 

model = sm.OLS(Y, X).fit()

# 3. Print the results
print(model.summary())

# INTERPRETATION:
# Look at the 'P>|t|' column for 'Ready_Partners'.
# If p < 0.05, it means Partner Readiness significantly impacts your readiness.
# Look at 'Coef': If it is positive (e.g., 0.4), then for every 1 point increase 
# in partner readiness, your readiness goes up by 0.4 points.