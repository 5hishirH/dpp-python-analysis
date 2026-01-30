from dataframe import df

import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x='Company_Size', y='Readiness_Score', data=df)
plt.show()