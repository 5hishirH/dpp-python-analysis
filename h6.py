# Hypothesis 06: Consumer demand for transparency influences readiness more strongly than government support.


from prep import df
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
