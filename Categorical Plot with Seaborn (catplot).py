import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the built-in Titanic dataset
data = sns.load_dataset('titanic')

# Create a categorical plot
sns.catplot(
    data=data,
    x="class",
    y="age",
    hue="sex",
    kind="swarm",
    palette="pastel",
    height=6,
    aspect=1.5
)

# Add a title
plt.title("Age Distribution by Class and Gender", fontsize=16)
plt.show()
