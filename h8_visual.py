from h8 import awareness, budget

import seaborn as sns
import matplotlib.pyplot as plt

# Visualizing it (Jitter Plot)
# Since many dots will overlap on a 1-5 scale, we add 'jitter' to see them better
sns.stripplot(x=awareness, y=budget, jitter=True, alpha=0.6)
plt.xlabel("Regulatory Awareness (Q15)")
plt.ylabel("Budget Allocation (Q8)")
plt.title("Does Awareness Drive Investment?")
plt.show()