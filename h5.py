# Hypothesis 05: (Biggest Barrier) Cost is the most significant barrier to adoption among suppliers.

from prep import df

barriers = df[['G1', 'G2', 'G3', 'G4', 'G5']]

# Calculate mean for each column and sort
barrier_means = barriers.mean().sort_values(ascending=False)

print("Ranking of Barriers (Highest = Biggest Problem):")
print(barrier_means)
