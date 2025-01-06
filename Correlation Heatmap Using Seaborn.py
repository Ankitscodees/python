import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample dataset
np.random.seed(42)
data = pd.DataFrame({
    'Variable 1': np.random.rand(100),
    'Variable 2': np.random.rand(100),
    'Variable 3': np.random.rand(100),
    'Variable 4': np.random.rand(100)
})

# Compute the correlation matrix
correlation_matrix = data.corr()

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, cbar_kws={"shrink": .8})
plt.title("Correlation Heatmap", fontsize=16)
plt.show()
