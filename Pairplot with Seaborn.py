import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the built-in Iris dataset
data = sns.load_dataset('iris')

# Create a pairplot
sns.pairplot(data, hue='species', palette='Set2', diag_kind='kde')

# Add a title
plt.suptitle("Pairplot of Iris Dataset", y=1.02, fontsize=16)
plt.show()
