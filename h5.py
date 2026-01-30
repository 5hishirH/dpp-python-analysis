# Hypothesis 05: Perceived consumer demand for transparency has a stronger influence on readiness than government support.

from dataframe import df
import statsmodels.api as sm

# D2: Gov_Support
# D3: Consumer_Demand
X = df[['D3', 'D2']]
Y = df['Readiness_Score']

X = sm.add_constant(X)

model = sm.OLS(Y, X).fit()

# Print summary to see Coefficients
print(model.summary())

# Look at the 'coef' column in the output:
# If Consumer_Demand (D3) coef > Gov_Support (D2) coef, your hypothesis is supported.
