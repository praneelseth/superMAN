import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Sample data
array_A = np.random.normal(loc=5, scale=1, size=100)
array_B = np.random.normal(loc=7, scale=1.5, size=100)
array_C = np.random.normal(loc=6, scale=1.2, size=100)

# Function to calculate mean and confidence interval
def mean_ci(data, confidence=0.95):
    mean = np.mean(data)
    sem = stats.sem(data)  # Standard Error of the Mean
    ci_range = sem * stats.t.ppf((1 + confidence) / 2., len(data) - 1)  # Confidence interval
    return mean, ci_range

# Calculate mean and confidence intervals for each array
means = []
cis = []
for array in [array_A, array_B, array_C]:
    mean, ci = mean_ci(array)
    means.append(mean)
    cis.append(ci)

# Create the bar plot
labels = ['Array A', 'Array B', 'Array C']
x = np.arange(len(labels))

fig, ax = plt.subplots()
bars = ax.bar(x, means, yerr=cis, capsize=5, color=['#1f77b4', '#ff7f0e', '#2ca02c'])

# Add labels and title
ax.set_ylabel('Average Value')
ax.set_title('Average Values with Confidence Intervals')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.yaxis.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
