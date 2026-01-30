from h3 import barrier_means
import matplotlib.pyplot as plt

barrier_means.plot(kind='bar')
plt.title("Biggest Barriers to DPP Adoption")
plt.ylabel("Average Agreement Score (1-5)")
plt.show()